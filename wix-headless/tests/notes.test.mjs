import assert from 'node:assert/strict';
import { test } from 'node:test';
import { readFileSync } from 'node:fs';
import ts from 'typescript';
const code = ts.transpileModule(readFileSync(new URL('../src/lib/notes.ts', import.meta.url), 'utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext } }).outputText;
const { summarize, homeNotes, matchesNote } = await import(`data:text/javascript;base64,${Buffer.from(code).toString('base64')}`);
const post = (n, pinned = false) => ({ slug: String(n), title: `Note ${n}`, excerpt: 'A short summary', contentText: 'Text with a hidden needle', pinned, pubDate: new Date(2026, 8, n), category: 'Work', tags: [{label:'Lorem', slug:'lorem'}, {label:'Ipsum',slug:'ipsum'}] });
test('summaries remain strictly below 50 words', () => {
 for (const n of [0,1,48,49,50,300]) assert.ok(summarize(Array(n).fill('word').join(' ')).split(/\s+/).filter(Boolean).length < 50);
 assert.equal(summarize('  one\n two  '), 'one two');
});
test('home shows at most two pins first, then newest other notes, without duplicates', () => {
 const result = homeNotes([post(1,true),post(2,true),post(3,true),post(4,true),post(5),post(6),post(7),post(8)]);
 assert.deepEqual(result.map(p => p.slug), ['4','3','8','7','6']);
 assert.equal(new Set(result.map(p=>p.slug)).size,5);
 assert.deepEqual(homeNotes([post(1),post(2)]).map(p=>p.slug), ['2','1']);
 assert.deepEqual(homeNotes([]),[]);
});
test('search includes full body and combines all selected topics and category', () => {
 assert.ok(matchesNote(post(1),'NEEDLE text',['lorem','ipsum'],'Work'));
 assert.ok(!matchesNote(post(1),'needle',['missing'],'Work'));
 assert.ok(!matchesNote(post(1),'needle',['lorem'],'Food'));
 assert.ok(!matchesNote(post(1),'absent',[]));
 assert.ok(matchesNote(post(1),'',[]));
});

"""Import a local snapshot without executing PHP. Usage: python scripts/import-legacy-archive.py SNAPSHOT"""
from pathlib import Path
from urllib.parse import urljoin, urlsplit, unquote, quote
import sys, re, json, shutil, unicodedata
from bs4 import BeautifulSoup, Comment

PROJECT = Path(__file__).resolve().parents[1]
LEGACY = Path(sys.argv[1]).resolve() if len(sys.argv)>1 else PROJECT.parent/'legacy-phrits'
DATA = PROJECT/'src/data'
PUBLIC = PROJECT/'public'
DATA.mkdir(parents=True, exist_ok=True)
urls = {'/':'/archive/','/recipes/':'/archive/recipes/'}
records=[]
warnings=[]
def read(path):
    raw=path.read_bytes()
    try: return raw.decode('utf-8')
    except UnicodeDecodeError: return raw.decode('cp1252')
def slugify(s):
    return re.sub('[^a-z0-9]+','-',unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()).strip('-') or 'index'
def register(path,url):
    key='/'+path.relative_to(LEGACY).as_posix()
    urls[key]=url
    if path.name in ('index.php','index.html'): urls[key.rsplit('/',1)[0]+'/']=url

def expanded(path,depth=0):
    if depth>8: raise ValueError('Recursive include '+str(path))
    raw=read(path)
    def include(m):
        target=(LEGACY/m[2].lstrip('/')) if '$www' in m[0] or m[2].startswith('/') else path.parent/m[2]
        # Head/nav/footer are supplied by the new layout.
        if any(x in target.name for x in ('header','footer','scripts','head.')): return ''
        return expanded(target.resolve(),depth+1) if target.is_file() else ''
    raw=re.sub(r'<\?php(.*?)\?>',lambda m: re.sub(r'\binclude\s*\(?\s*(\$www\s*\.\s*)?[\'\"]([^\'\"]+)[\'\"]\s*\)?\s*;',include,m[1]) if 'include' in m[1] else '',raw,flags=re.S)
    return re.sub(r'\b(require|chdir)\s*\([^;]+;','',raw)

recipe_paths=[]
for p in sorted((LEGACY/'recipes').glob('*/index.php')):
    raw=read(p)
    if '<h1' not in raw and '<html' not in raw.lower(): continue
    recipe_paths.append(p)
    register(p,'/archive/recipe/?slug='+p.parent.name)

core=[('resume','Résumé','Professional history','resume/index.php'),('notary-public','Notary Public','Public service','notary_public/index.php'),('writing/rule-number-one','Rule Number One','Writing','writing/rule_number_one/index.php'),('writing/family-goals','Family Goals','Writing','writing/family_goals/index.php'),('writing/glass-mountain','Glass Mountain','Writing','writing/glass_mountain/index.php'),('writing/why-i-left-it','Why I’m Leaving IT','Writing','writing/leaving_it/index.php'),('writing/support-the-troops','Support the Troops','Writing','writing/support_the_troops/index.php'),('food/food-and-cooking-terms','Food and Cooking Terms','Food resources','food_resources/food_glossary/index.php'),('food/fat-tom','Your Friend in the Kitchen: FAT TOM','Food resources','food_resources/fat_tom/index.php'),('food/popcorn-post','The Popcorn Post','Food resources','food_resources/popcorn_post/index.php'),('food/meat-and-food-safety','Meat and Food Safety','Food resources','food_resources/meat_safety/index.php'),('community','Community','About','community/index.php'),('miscellany','Miscellany','About','miscellany/index.php'),('credits','Credits','About','credits/index.php'),('hire-me','Hire Me','Professional history','hire_me/index.php'),('writing','Writing','Writing','writing/index.php'),('food','Food Resources','Food resources','food_resources/index.php')]
for slug,title,section,relative in core:
    p=LEGACY/relative
    records.append((p,slug,title,section))
    register(p,'/archive/item/?slug='+slug)

for year in ('2007','2012'):
    p=LEGACY/('resume/FKnack_Resume_IT_'+year+'.html')
    slug='resume/'+year
    records.append((p,slug,'IT Résumé ('+year+')','Professional history'))
    register(p,'/archive/item/?slug='+slug)

cookroot=LEGACY/'writing/ward_cookbook' 
for p in sorted(cookroot.rglob('*.html')):
    if p.name=='index.html' and (p.parent/'cookbook.html').exists(): continue
    soup=BeautifulSoup(read(p),'html.parser')
    title=soup.title.get_text(' ',strip=True) if soup.title else p.stem.title()
    rel=p.relative_to(cookroot)
    category=rel.parent.as_posix().replace(' & ',' and ').title()
    slug='demeters-harvest/'+('index' if p.name=='cookbook.html' else ('alphabetical-index' if p.name=='recipe_index.html' else slugify(category)+'/'+('index' if p.name=='chapter_index.html' else slugify(title))))
    records.append((p,slug,title,'Demeter’s Harvest'+(' · '+category if category!='.' else '')))
    register(p,'/archive/item/?slug='+slug)
urls['/writing/ward_cookbook/']=urls['/writing/ward_cookbook/index.html']=urls['/writing/ward_cookbook/cookbook.html']
# Legacy shorthand URLs are aliases, not duplicate content.
for p in LEGACY.rglob('index.php'):
    key='/'+p.relative_to(LEGACY).as_posix()
    if key in urls: continue
    m=re.search(r'include\s*\(?\s*\$www\s*\.\s*[\'\"]([^\'\"]+)[\'\"]',read(p))
    if m:
        target='/'+m[1].lstrip('/')
        if target in urls: register(p,urls[target])

for slug,title,section,relative in core:
    if relative.startswith('writing/') or relative.startswith('food_resources/'):
        urls['/'+Path(relative).parent.name+'/']='/archive/item/?slug='+slug
urls.update({'':'/archive/','/index.php':'/archive/','/index.html':'/archive/','/ward_cookbook/':urls['/writing/ward_cookbook/'], '/writing/ward_cookbook':urls['/writing/ward_cookbook/'],'/itProfessional':'/archive/item/?slug=resume','/content/glossary.php':'/archive/item/?slug=food/food-and-cooking-terms','/cooking_school/glossary/':'/archive/item/?slug=food/food-and-cooking-terms','/content/popcorn_post.php':'/archive/item/?slug=food/popcorn-post','/recipes/tomato_sauce.php':'/archive/recipe/?slug=tomato_sauce'})

def rewrite(value,path,anchor=False):
    # Some legacy anchors contain a stray quote inside the URL value.
    value=value.strip().rstrip('"\'')
    if value in ('moist_heat','stock') and 'food_glossary' in str(path): return '#'+value
    if value.startswith(('#','mailto:','tel:','data:')): return value
    parsed=urlsplit(urljoin('https://phrits.com/'+path.relative_to(LEGACY).as_posix(),value))
    if parsed.hostname not in ('phrits.com','www.phrits.com'):
        return '#' if anchor and parsed.scheme in ('http','https') else value
    key=unquote(parsed.path)
    if key in urls: return urls[key]+('#'+parsed.fragment if parsed.fragment else '')
    local=LEGACY/key.lstrip('/')
    if local.is_file() and local.suffix.lower() not in ('.php','.html'):
        dest=PUBLIC/'archive-legacy'/key.lstrip('/')
        dest.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(local,dest)
        return '/archive-legacy/'+quote(key.lstrip('/'),safe='/')+('#'+parsed.fragment if parsed.fragment else '')
    if key.startswith('/food_books'): return None
    warnings.append({'source':str(path.relative_to(LEGACY)),'target':value})
    # Never leave a migrated link pointing back at the retired site.
    return '#'

def fragment(path,recipe=False):
    soup=BeautifulSoup(expanded(path),'html.parser')
    body=(soup.select_one('div.recipe') if recipe else soup.select_one('#main')) or soup.body or soup
    for c in body.find_all(string=lambda x:isinstance(x,Comment)): c.extract()
    for t in body.select('script,style,nav,header,footer'): t.decompose()
    for t in body.find_all(True):
        for attr in ('href','src'):
            if t.has_attr(attr):
                original=t[attr]
                value=rewrite(original,path,anchor=(attr=='href' and t.name=='a'))
                if value is None: t.unwrap(); break
                t[attr]=value
                if t.name=='a' and value=='#':
                    lower=original.lower()
                    label=t.get_text(' ',strip=True).lower()
                    if 'ucm082294' in lower and label=='here':
                        t.string='Here (FDA food-safety guidance; old link unavailable)'
                    elif 'howstuffworks.com' in lower and label=='this':
                        t.string='this (HowStuffWorks: eating raw meat; original link could not be verified)'
        if t.name:
            t.attrs={k:v for k,v in t.attrs.items() if k in {'href','src','alt','title','id','name','class','colspan','rowspan'}}
    return body

index=BeautifulSoup(expanded(LEGACY/'recipes/index.php'),'html.parser')
metadata={}
for row in index.select('div.recipe'):
    anchor=row.select_one('h2 a')
    if not anchor: continue
    slug=anchor['href'].strip('/').split('/')[-1]
    tags=sorted(set(x.get_text(' ',strip=True).lower() for x in row.select('.dietary')))
    index_image=row.select_one('img[src]')
    index_image=rewrite(index_image['src'],LEGACY/'recipes/index.php') if index_image else None
    for t in row.select('h2'): t.decompose()
    full=re.sub(r'\s+',' ',row.get_text(' ',strip=True)).strip()
    note=re.search(r'\[([^]]+)\]',full)
    dietary_note=note[1].strip() if note else ''
    description=re.sub(r'\[[^]]*\]','',full).strip()
    canonical=urls.get('/recipes/'+slug+'/', '')
    if '?slug=' in canonical: slug=canonical.split('?slug=')[1]
    metadata[slug]={'description':description,'tags':tags,'dietaryNote':dietary_note,'indexImage':index_image}
recipes=[]
for p in recipe_paths:
    body=fragment(p,True)
    h=body.find('h1')
    title=h.get_text(' ',strip=True) if h else p.parent.name.replace('_',' ').title()
    images=list(dict.fromkeys(t['src'] for t in body.select('img[src]')))
    recipes.append({'slug':p.parent.name,'title':title,'html':str(body),**metadata.get(p.parent.name,{'description':'','tags':[]}),'images':images,'image':images[0] if images else None,'sourcePath':p.relative_to(LEGACY).as_posix()})
items=[]
for p,slug,title,section in records:
    body=fragment(p)
    items.append({'slug':slug,'title':title,'section':section,'html':''.join(map(str,body.contents)),'sourcePath':p.relative_to(LEGACY).as_posix()})
# Copy the original index photograph even though the index is re-rendered.
rewrite('/images/board_and_knife.jpg',LEGACY/'recipes/index.php')
for name,obj in [('archive-recipes',recipes),('archive-items',items),('legacy-redirects',urls),('archive-import-report',{'recipes':len(recipes),'archiveItems':len(items),'legacyUrlCount':len(urls),'unresolvedLegacyLinks':warnings,'aliases':{k:v for k,v in urls.items() if k.startswith('/recipes/')}})]:
    (DATA/(name+'.json')).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'recipes':len(recipes),'archiveItems':len(items),'unresolvedLinks':len(warnings)}))
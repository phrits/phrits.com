export interface NoteSummary {
  slug: string;
  title: string;
  excerpt: string;
  contentText: string;
  pinned: boolean;
  pubDate: Date;
  category?: string;
  tags: Array<{ label: string; slug: string }>;
}

export function summarize(text: string): string {
  const words = text.trim().split(/\s+/).filter(Boolean);
  return words.slice(0, 49).join(' ') + (words.length > 49 ? '…' : '');
}
export function newest<T extends NoteSummary>(posts: T[]): T[] {
  return [...posts].sort((a, b) => b.pubDate.getTime() - a.pubDate.getTime() || a.slug.localeCompare(b.slug));
}
export function homeNotes<T extends NoteSummary>(posts: T[]): T[] {
  const ordered = newest(posts);
  const pins = ordered.filter(post => post.pinned).slice(0, 2);
  return [...pins, ...ordered.filter(post => !post.pinned)].slice(0, 5);
}
export function matchesNote(post: NoteSummary, query: string, topics: string[], category = ''): boolean {
  const haystack = [post.title, post.excerpt, post.contentText, post.category, ...post.tags.map(tag => tag.label)].join(' ').toLocaleLowerCase();
  return query.toLocaleLowerCase().trim().split(/\s+/).every(word => haystack.includes(word))
    && topics.every(topic => post.tags.some(tag => tag.slug === topic))
    && (!category || post.category === category);
}

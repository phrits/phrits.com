import type { BlogPost } from './blog';
const lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante venenatis dapibus posuere velit aliquet. Donec ullamcorper nulla non metus auctor fringilla. Maecenas faucibus mollis interdum. Sed posuere consectetur est at lobortis.';
export const samplePosts: BlogPost[] = Array.from({ length: 16 }, (_, i) => ({
  slug: `sample-${i + 1}`,
  title: ['Lorem ipsum dolor sit amet', 'Consectetur adipiscing elit', 'Integer posuere erat a ante', 'Donec ullamcorper nulla'][i % 4] + ` · ${i + 1}`,
  excerpt: lorem,
  contentText: `${lorem} ${i === 15 ? 'Vestibulum' : ''}`,
  pinned: i < 4,
  pubDate: new Date(Date.UTC(2026, 8, 26 - i, 16)),
  category: i % 2 ? 'Sample category B' : 'Sample category A',
  tags: [{ label: 'Lorem', slug: 'lorem' }, ...(i % 2 ? [{ label: 'Ipsum', slug: 'ipsum' }] : [])],
  richContent: null,
}));

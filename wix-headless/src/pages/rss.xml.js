import rss from '@astrojs/rss';
import { queryBlogPosts } from '../lib/blog';
import { SITE_DESCRIPTION, SITE_TITLE } from '../consts';

export async function GET(context) {
  let posts = [];
  try {
    posts = await queryBlogPosts();
  } catch (error) {
    console.error('[blog] RSS query failed:', error);
  }
  return rss({
    title: SITE_TITLE,
    description: SITE_DESCRIPTION,
    site: context.site,
    items: posts.map((post) => ({
      title: post.title,
      pubDate: post.pubDate,
      description: post.excerpt,
      link: `/blog/${post.slug}/`,
    })),
  });
}

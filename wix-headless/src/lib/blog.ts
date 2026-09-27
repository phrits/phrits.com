import { categories, posts, tags } from "@wix/blog";
import { media } from "@wix/sdk";
import { summarize } from "./notes";

export interface BlogPost {
  slug: string;
  title: string;
  excerpt: string;
  contentText: string;
  pinned: boolean;
  coverImageUrl?: string;
  pubDate: Date;
  category?: string;
  richContent: unknown;
  tags: Array<{ label: string; slug: string }>;
}

function createResolver() {
  const fetchCategory = (id: string) => categories.getCategory(id);
  const fetchTag = (id: string) => tags.getTag(id);
  const categoryCache = new Map<string, ReturnType<typeof fetchCategory>>();
  const tagCache = new Map<string, ReturnType<typeof fetchTag>>();
  return async function resolvePost(item: any): Promise<BlogPost> {
  const resolvedCategories = await Promise.all(
    (item.categoryIds ?? []).map(async (id: string) => {
      if (!categoryCache.has(id)) categoryCache.set(id, categories.getCategory(id));
      const { category } = await categoryCache.get(id)!;
      return category;
    }),
  );
  const resolvedTags = await Promise.all(
    (item.tagIds ?? []).map(async (id: string) => {
      if (!tagCache.has(id)) tagCache.set(id, tags.getTag(id));
      const tag = await tagCache.get(id)!;
      return { label: tag.label ?? "", slug: tag.slug ?? "" };
    }),
  );
  const coverImageUrl = item.media?.wixMedia?.image
    ? media.getImageUrl(item.media.wixMedia.image).url
    : undefined;
  const pubDate = new Date(item.firstPublishedDate ?? item._createdDate ?? Date.now());
  return {
    slug: item.slug ?? "",
    title: item.title ?? "Untitled note",
    excerpt: summarize(item.excerpt || item.contentText || ""),
    contentText: item.contentText ?? "",
    pinned: Boolean(item.featured || item.pinned),
    coverImageUrl,
    pubDate,
    category: resolvedCategories[0]?.label,
    richContent: item.richContent,
    tags: resolvedTags.filter((tag) => tag.label && tag.slug),
  };
  };
}

export async function queryBlogPosts(limit?: number): Promise<BlogPost[]> {
  let page = await posts.queryPosts({ fieldsets: ["CONTENT_TEXT"] })
    .descending("firstPublishedDate").limit(100).find();
  const items = [...page.items];
  while (page.hasNext() && (!limit || items.length < limit)) {
    page = await page.next();
    items.push(...page.items);
  }
  return Promise.all((limit ? items.slice(0, limit) : items).map(createResolver()));
}

export async function getPostBySlug(slug: string): Promise<BlogPost | null> {
  const { items } = await posts
    .queryPosts({ fieldsets: ["RICH_CONTENT", "CONTENT_TEXT"] })
    .eq("slug", slug)
    .find();
  return items?.[0] ? createResolver()(items[0]) : null;
}

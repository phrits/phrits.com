# Notes

Write and publish real articles in the existing Wix Blog. This frontend reads published posts, categories, tags, and article content from that blog.

## Pins

Mark a post as **featured** in Wix Blog to pin it in this frontend. Existing native pinned posts are also recognized. There is no frontend limit on the total number of pins. Remove the featured flag (and native pinned status, if set) to unpin.

Pins sort by original publication date, newest first. Home displays the newest two pins, followed by the newest non-pinned articles, up to five titles total. If fewer articles exist, it shows fewer lines.

The Notes index displays three pins and ten non-pinned recent articles initially. A Continue button appears for four or more pins, revealing three more per click. A separate Continue button appears for eleven or more recent articles, revealing ten more per click. Articles are never repeated in both sections. Expanding lists lengthens the page with ordinary browser scrolling; there are no nested scrolling panels. On phones the tools stack above the articles and titles wrap.

## Summaries, organization, and search

The excerpt supplies each summary. When empty, the article's plain text supplies it. Summaries stop at 49 words, with an ellipsis when shortened.

The first assigned category supplies the category label/filter. Tags are topics. Topic checkboxes are multi-select: articles must match all selected topics. Search covers title, summary, full article text, category, and topic labels. Category, topics, and search work together. Filter URLs can be bookmarked or shared. Tags below articles link back to a filtered index.

The frontend follows every Wix results page; older articles are not silently cut off at the first API page. The current implementation renders the full search index on the page, appropriate for a personal collection. If the collection reaches thousands of long articles, move full-text filtering to a paginated server search.

## Lorem Ipsum samples

Append `?samples=1` to Home or Notes to see the separate sample preview:

- `/?samples=1`
- `/blog?samples=1`
- `/blog/sample-1/?samples=1`

Sixteen short sample entries exercise both Continue controls (four pins and twelve recent items). The sample article demonstrates headings, emphasis, quotation, lists, links, and a code block. Samples do not create or publish Wix posts, appear in RSS, or mingle with real content. Preview pages carry noindex/nofollow metadata.

## Editing and publishing

The Astro app is in the `wix-headless` folder on the `wix-headless` branch of `phrits/phrits.com`. Clone that branch with GitHub Desktop, then open the `wix-headless` folder in VS Code. Use GitHub Desktop to fetch/pull code changes and commit/push your own changes.

The branch includes `wix.config.json`, which connects the app to your Wix site. Login credentials and local session state stay out of Git. From Command Prompt in the app folder, run `npm ci`, then `npx wix build` and `npx wix preview` to test. `npx wix release` publishes to the live site.

Normal articles appear at `/blog`; use the sample URLs above to inspect the full layout before you have enough published articles.

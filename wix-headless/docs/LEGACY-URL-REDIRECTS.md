# Legacy URL redirects

The migration extracts **319 legacy path aliases** into `src/data/legacy-redirects.json`. The catch-all route `src/pages/[...legacy].astro` issues a permanent 301 redirect for known legacy addresses, including old recipe PHP paths, and returns a site-styled 404 for unknown paths.

The route, map, importer, and archive link updates are included in this branch. Internal links point to migrated pages or copied legacy assets; external http(s) anchors become `#`; two vague broken or uncertain links get short descriptions.

# Legacy URL redirects

The migration extracts **319 legacy path aliases** into `src/data/legacy-redirects.json`. The catch-all route `src/pages/[...legacy].astro` issues a permanent 301 redirect for each known legacy address, including old recipe PHP paths, and returns a site-styled 404 for unknown paths.

The route and redirect map are now committed to this branch. When you copy the Astro app from your existing Windows project into this folder, preserve these two files or overlay the accompanying redirect patch. The patch also updates `scripts/import-legacy-archive.py` and imported archive data so internal links lead to migrated pages, external http(s) anchors become `#`, and two broken/uncertain generic links receive short descriptions.

The source project remains in `C:\\Unsynched\\phrits-wix-archive-checkpoint-2026-09-21\\phritscom`. Do not copy credentials or generated files (`.env*`, `.wix/`, `.wrangler/`, `.astro/`, `node_modules/`, or `dist/`) into Git.

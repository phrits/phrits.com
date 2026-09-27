# Wix Headless branch

This folder holds the Wix Headless handoff and legacy redirect implementation. The full Astro app and imported archive content are not yet in this branch.

The redirect implementation is already present:

- `src/data/legacy-redirects.json` — 319 known legacy paths mapped to migrated destinations.
- `src/pages/[...legacy].astro` — 301 redirects for known paths and a styled 404 for unknown paths.
- `scripts/import-legacy-archive.py` — link rewriting and redirect-map generation.
- `docs/LEGACY-URL-REDIRECTS.md` — migration notes.

`wix.config.json` is ignored because it contains this project's site and app identifiers. Keep your existing linked copy local.

When the app source is present, use VS Code for editing and GitHub Desktop to fetch/pull assistant commits and commit/push your changes. From the app folder, `npx wix dev` starts local development, `npx wix build` builds the project, `npx wix preview` uploads a test version, and `npx wix release` publishes to the live Wix site. GitHub and Wix preview/release are separate actions.

# phrits.com — Wix Headless

This folder contains the Astro site connected to Wix Headless, the migrated legacy archive, recipes, Notes/blog, and URL redirects.

## Edit and preview

Open this `wix-headless` folder in VS Code. Use GitHub Desktop to switch to the `wix-headless` branch and fetch/pull updates before editing. Commit and push your changes to that branch when ready.

From this folder:

- `npm install` installs dependencies, including the Wix CLI.
- `npm run dev` starts local development.
- `npm run build` builds the site.
- `npm run preview` uploads a test version to Wix.
- `npm run release` publishes to the connected Wix site.

A Git commit updates GitHub. Wix preview and release are separate actions.

## What's here

- `src/pages/` — site pages, archive, recipe index, Notes, and legacy URL handling.
- `src/data/archive-items.json` and `archive-recipes.json` — imported archive and recipe records.
- `public/archive-legacy/` — original archive media and downloadable files.
- `src/data/legacy-redirects.json` — old URLs mapped to local pages or the requested external-link fallback.
- `docs/NOTES-GUIDE.md` — how to add, pin, tag, and summarize Notes.

The Wix project configuration is included so the branch can build against the connected site. Wix credentials and session state are excluded by `.gitignore`.

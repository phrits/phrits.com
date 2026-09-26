# Wix Headless app

This folder is the app root for the Astro version of phrits.com. The `main` branch remains the legacy PHP site while this migration is prepared.

## Add the existing app source

Copy the project files from `C:\\Unsynched\\phrits-wix-archive-checkpoint-2026-09-21\\phritscom` into this folder. Copy the contents of that directory, including `src`, `public`, `docs`, `scripts`, `tests`, `package.json`, `package-lock.json`, `astro.config.mjs`, `wix.config.json`, and `tsconfig.json`. Keep the `.gitignore` already in this folder.

Do not copy `.env*`, `.wix/`, `.wrangler/`, `.astro/`, `node_modules/`, or `dist/`. They contain local credentials/session state or generated files. Keep your existing Wix credentials local; do not commit them.

## Develop, preview, and publish

Open this folder in VS Code. Use GitHub Desktop when you are ready to commit and push code to the `wix-headless` branch.

From a terminal opened in this folder:

- `npm ci` installs the locked dependencies.
- `npx wix dev` starts the local development environment.
- `npx wix build` checks and builds the project.
- `npx wix preview` uploads a test version to Wix and returns preview URLs. It does not publish that version to the live site.
- `npx wix release` publishes the current project to the live Wix site.

Wix preview/release and GitHub commit/push are separate actions. Test with preview first; commit when the changes are ready for the repository, and release only when you intend them to be live.

# Wix Headless app

This folder is the app root for the Astro version of phrits.com. The `main` branch remains the legacy PHP site while this migration is prepared.

## Add the existing app source

Copy the project files from `C:\\Unsynched\\phrits-wix-archive-checkpoint-2026-09-21\\phritscom` into this folder. Copy the contents of that directory, including `src`, `public`, `docs`, `scripts`, `tests`, `package.json`, `package-lock.json`, `astro.config.mjs`, `wix.config.json`, and `tsconfig.json`.

Do not copy `.env*`, `.wix/`, `.wrangler/`, `.astro/`, `node_modules/`, or `dist/`. They contain local credentials/session state or generated files. Keep your existing Wix credentials local; do not commit them.

## Edit and release

Open this folder in VS Code. Use GitHub Desktop to review changes, commit them on `wix-headless`, and push to GitHub. From a terminal opened in this folder, install dependencies with `npm ci`, run `npx wix dev` for local preview, and run `npx wix build` before a release. Wix hosting release is a separate step from pushing the Git branch.
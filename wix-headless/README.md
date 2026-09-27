# Wix Headless app

This folder contains the Astro app for phrits.com. The repository's `main` branch remains the legacy PHP site; this app lives in `wix-headless/` on the `wix-headless` branch.

## Local Wix connection

The site-specific `wix.config.json` is intentionally excluded from Git. Copy that one file from your existing linked Wix project into this folder on your computer. It tells the Wix CLI which site and private app to use. Keep it local.

## Develop, preview, and publish

Open this folder in VS Code. Use GitHub Desktop to fetch/pull assistant commits, review your changes, and commit/push your own changes.

From a terminal opened in this folder:

- `npm ci` installs the locked dependencies.
- `npx wix dev` starts the local development environment.
- `npx wix build` checks and builds the project.
- `npx wix preview` uploads a test version to Wix and returns preview URLs. It does not publish that version to the live site.
- `npx wix release` publishes the current project to the live Wix site.

Wix preview/release and GitHub commit/push are separate actions. You can test with preview before committing; release only when you intend the code to be live.

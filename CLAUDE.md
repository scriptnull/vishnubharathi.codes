# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Personal website/blog for Vishnu Bharathi (`scriptnull`), served at https://vishnubharathi.codes via GitHub Pages. Built with the [Hexo](https://hexo.io/) static site generator (pinned to v5.3.0) using a [forked cactus theme](https://github.com/scriptnull/hexo-theme-cactus).

## Setup & commands

The theme is **not vendored** in this repo (despite the `.gitmodules` entry, `themes/cactus` is cloned, not initialized as a submodule, in CI). Local setup:

```sh
npm i
git clone https://github.com/scriptnull/hexo-theme-cactus.git themes/cactus
```

- `npm run dev` — generate site and serve at http://localhost:4000 (`hexo generate && hexo server`)
- `./package.sh` — production build: runs `hexo generate`, then replaces `./docs` with the generated `public/`, restores `CNAME`, `.well-known/atproto-did`, and `.nojekyll`
- `npx hexo new post "Title"` — scaffold a new post in `source/_posts/` (uses `scaffolds/post.md`)

There is no test or lint suite — this is a content repo.

## Content structure

- `source/_posts/*.md` — blog posts (~113). Front matter: `title`, `date`, `tags` (array). Permalink pattern is `blog/:title/`.
- `source/_drafts/` — unpublished drafts (`render_drafts: false`)
- `source/<name>/index.md` — standalone pages: `shipped/`, `quotes/`, `books/`, `talks/`
- `source/images/`, `source/keybase.txt`, `source/.well-known/` — static assets passed through
- `_config.yml` — Hexo + theme config (site metadata, nav, theme_config)
- `scaffolds/` — templates for `hexo new`

## Deployment (important)

GitHub Pages serves the **committed `docs/` directory** (`public_dir: public` is built, then moved to `docs/` by `package.sh`). `docs/` is generated output but **is checked into git** — it is not in `.gitignore` (only `public/` is).

CI workflow `.github/workflows/deploy.yml` runs on every push to `master`:
1. Always builds the site and creates a `Generated site :sparkles:` commit.
2. **Only pushes the generated commit if the triggering commit message starts with `[deploy]`** (`startsWith(github.event.head_commit.message, '[deploy]')`).

So: to publish a content change, the human-authored commit on `master` must be prefixed with `[deploy]`. A non-`[deploy]` commit builds but does not publish. `manual-deploy.yml` (workflow_dispatch) builds and pushes unconditionally.

When editing content, you generally do **not** need to hand-edit `docs/` — CI regenerates it. Avoid manually committing `docs/` changes unless reproducing the CI build locally via `./package.sh`.

## Conventions

- Commit messages for content/site changes that should go live are prefixed `[deploy]` (e.g. `[deploy] add a new quote`). CI's own build commits use `Generated site :sparkles:`.
- New quotes in `source/quotes/index.md` are added to the **top** of the list (just after the intro line, newest first), not appended to the bottom.
- Theme changes are made in the separate `hexo-theme-cactus` repo, not here; this repo only consumes it.

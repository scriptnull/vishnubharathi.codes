---
name: new-blog-post
description: Draft a new blog post for vishnubharathi.codes from free-form writing typed in the session. Use when the user wants to write/draft/publish a blog post, dictates post content, or says things like "new blog post", "draft a post", "let's write a blog". Preserves the author's voice, fixes grammar conservatively, and handles Hexo front matter, filenames, and the no-deploy commit convention.
---

# New Blog Post

Help Vishnu (`scriptnull`) turn free-form writing typed in the session into a
finished Hexo blog post in this repo. One session = one post.

## Golden rule: preserve the author's voice

This is the most important constraint. The author's style is the product.

- **Apply silently:** obvious typos, misspellings, doubled words, missing/wrong
  punctuation, capitalization, broken Markdown.
- **Do NOT apply automatically:** rewording sentences, restructuring,
  tightening, changing tone, "improving" phrasing. The author writes
  conversational, first-person, sometimes-fragmentary prose on purpose.
- **Suggest separately:** collect larger grammar/flow/clarity issues into a
  short list presented *after* the draft (see Workflow step 4). The author
  accepts or rejects each. Never bake these in unprompted.
- When unsure whether something is a typo or intentional voice, leave it and
  mention it in the suggestions list.

Study existing posts in `source/_posts/` (e.g. `why-i-blog.md`, `short.md`,
`rlwrap.md`) to internalize the voice before editing.

## Workflow

1. **Collect the writing.** The user types the post body free-form in the
   thread, possibly across multiple messages. Treat it as raw material. Ask
   for the title and tags if not given. Don't start editing until they signal
   the draft is complete (or ask if it's ambiguous).

2. **Determine the filename.** Lowercase kebab-case derived from the title:
   spaces → hyphens, drop punctuation. Example: "Why I Blog" →
   `why-i-blog.md`. Place in `source/_posts/`. Check the file doesn't already
   exist.

3. **Write the file** to `source/_posts/<slug>.md` with front matter:

   ```
   ---
   title: <Title As Typed>
   date: <YYYY-MM-DD HH:MM:SS>
   tags: ["tag1", "tag2"]
   ---

   <body, with only silent fixes applied>
   ```

   - `date`: use the current date/time. Get it with `date "+%Y-%m-%d %H:%M:%S"`.
   - `tags`: JSON-style array of quoted strings, lowercase, as the existing
     posts do. Reuse tags already used in the blog where they fit (grep
     `source/_posts/` for `tags:` to see the vocabulary).
   - Keep the body faithful to what was typed — only silent fixes from the
     Golden Rule.

4. **Present suggestions.** After writing, give the user a concise numbered
   list of the larger grammar/flow/clarity items you deliberately did NOT
   apply, each with the original text and your proposed change. Wait for the
   user to pick which to apply, then apply only those.

5. **Commit WITHOUT publishing.** Once the user is happy:
   - Commit to the current branch with a clear message that does **NOT** start
     with `[deploy]`. CI builds but does not publish non-`[deploy]` commits, so
     this is intentionally a safe, unpublished state.
   - Example message: `add blog post: <title>` (no `[deploy]` prefix).
   - Do **not** hand-edit or commit the `docs/` directory — CI regenerates it.
   - Push with `git push -u origin <current-branch>`.

6. **Tell the user how to publish.** Remind them: to actually go live, a
   commit on `master` must be prefixed `[deploy]` (e.g. they merge and the
   merge/commit message starts with `[deploy]`, or they add a follow-up
   `[deploy]` commit). Do not publish for them unless explicitly asked.

## TODO markers

Two special placeholders may appear in the author's writing:

- **TK** — a TODO for the author (Vishnu). Leave these in the post as-is; do
  not fill them in or remove them. After writing the file, list any TK markers
  you found so the author knows what still needs to be completed before
  publishing.
- **TKAI** — a TODO for the coding assistant (you). When you see TKAI in the
  draft, treat it as an instruction to fill in that section yourself. Replace
  the TKAI marker with the requested content, applying the same voice-preservation
  rules as the rest of the post. Mention what you filled in when presenting
  the draft.

## Notes

- Drafts dir (`source/_drafts/`, `render_drafts: false`) exists but the chosen
  flow is straight-to-`_posts` with a non-`[deploy]` commit. Use `_drafts/`
  only if the user explicitly asks for a draft.
- Permalink is `blog/:title/`, derived from the filename slug — get the slug
  right.
- No test/lint suite; this is a content repo. No need to build locally unless
  the user wants to preview with `npm run dev`.
- Don't add a PR unless the user explicitly asks.

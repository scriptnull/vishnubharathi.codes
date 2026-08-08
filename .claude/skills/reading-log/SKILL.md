---
name: reading-log
description: Draft a numbered "Reading Log #N" post for vishnubharathi.codes from photos of bullet journal pages, resolving blog links from Readwise. Use whenever the author shares pictures/scans of their daily log or journal spread and wants a reading log, a reading roundup, or a post about what they read this week — and also when they just say "reading log", "reading log #3", "here are my journal entries for the week", or hand over notebook photos with `B:` and `BL:` entries in them. Handles the image OCR prep, the Readwise link lookup, the Hexo front matter, and the no-deploy commit convention.
---

# Reading Log

Turn photos of Vishnu's (`scriptnull`) bullet journal into a numbered reading
log post in this repo. The journal is the source of truth; your job is to
transcribe it faithfully, attach real links, and get out of the way.

The [`new-blog-post`](../new-blog-post/SKILL.md) skill governs voice, TK
markers, and the commit convention — all of it applies here. Read it if you
haven't. This skill covers what's specific to reading logs.

## What you're looking for

Each journal page is a `DAILY LOG` with a date header like `29.7.WE`. Lines
carry short prefixes. Exactly two of them are in scope:

| Prefix | Meaning |
|---|---|
| `B:` | A book, usually with a page range |
| `BL:` | A blog post |

Everything nested under a `B:` or `BL:` line — the dashes, the quoted
passages, the half-finished thoughts — is his commentary on that item, and it
is the actual content of the post. The titles are just scaffolding.

**Every other line on the page is a no-op.** Don't transcribe it, don't
summarise it, don't ask about it, and don't describe what those lines are —
here, in your reply, or anywhere else. This is a private journal that happens
to contain two publishable lines a day; treat the rest as if it weren't
there. If a line is ambiguous, it's out.

## Workflow

### 1. Read the pages

Phone photos of a notebook come in rotated and too low-resolution to read at
full-page scale. Prep them first:

```sh
python3 .claude/skills/reading-log/scripts/prep_journal_images.py \
  <image paths> --out <scratchpad>/journal
```

Then read the crops. Two or three at a time in parallel is fine. If the text
comes out sideways or upside down, rerun with `--rotate 0` or `--rotate 90`.
If a specific line stays ambiguous, crop and upscale just that line rather
than squinting — a wrong book title is worse than an extra tool call.

Sort the pages into date order yourself, from the date headers. Upload order
and filename order are both unreliable.

### 2. Resolve the blog links from Readwise

He reads blogs on paper, so anything with a `BL:` marker was printed, which
means it carries the `printed` tag in Readwise. That tag is the lookup table:

```
reader_list_documents(tag=["printed"], limit=50,
  response_fields=["title", "url", "source_url", "author", "site_name", "created_at"])
```

Match journal titles against it and use `source_url` — the original article —
not `url`, which is the Readwise reader link. The `author` field is often an
RSS feed name (`seangoedecke.com RSS feed`, `Murat (noreply@blogger.com)`);
clean it up to the human's name where you know it, and fall back to the site
name when you don't.

Handwritten titles drift from the real ones ("5 lessons at 60" for *5 Lessons
at 50*), so trust the Readwise title over your reading of the page. If an
entry has no match, leave the title unlinked with a `TK` next to it rather
than guessing a URL — a wrong link is the one error a reader will notice.

Don't try to fetch the articles themselves to fill in context. Several of
these sites block automated fetches, and the notes should be his words about
the piece, not a summary you generated.

### 3. Work out the number

```sh
ls source/_posts/reading-log-*.md
```

The next one continues the sequence. File is `source/_posts/reading-log-N.md`,
permalink `/blog/reading-log-N/`.

**Quote the title in the front matter.** `title: Reading Log #1` parses as
`Reading Log` — YAML treats the ` #` as the start of a comment and silently
drops the number, which you won't notice until the post is live with the
wrong name.

```yaml
title: "Reading Log #1"
tags: ["reading", "books", "blogging"]
```

### 4. Write the post

Structure — intro prose with no heading above it, then blogs, then books:

```markdown
<intro paragraphs>

## Blogs

- [Title](source_url)

  <his notes>

  > <anything he quoted from the piece>

## Books

- **Title**

  (read N pages)

  <his notes>
```

Blogs come before books: there are usually a dozen of them to two books, and
they're the part he has the most to say about.

Entries are **bullet points, not headings** — the title and link sit on the
point, the notes are indented beneath it. This is a log; a list reads like
one, and a page of `###` headings for thirteen short entries does not. No
author bylines on the points; the link carries that.

For books, give the total pages read across the week, not the per-day ranges.
He tracks ranges in the journal to know where to resume, not to publish.

**Keep the notes tight — roughly a short paragraph per entry.** The journal
holds several fragmentary lines per item, and dumping all of them in makes
the draft baggy in a way that takes him longer to cut than to write. Merge
the fragments into one or two sentences that carry the point and drop the
throwaways. He will expand the entries he cares about with things the journal
never held — a link to a related post, what happened when he tried the idea —
so a lean, accurate draft is more useful to him than an exhaustive one.

Keep his sentences where you keep them. Expanding shorthand into a sentence
is fine and necessary ("Great article, esp relevant..." → "Great article,
especially relevant..."); rewriting is not. Anything he wrote inside quote
marks was quoted from the article, so set it as a blockquote.

The intro is the one part with no journal source, so you have to write it.
It's a short personal lead-in — what's going on with his reading lately —
ending with the date range, e.g. "here is what I read from 27<sup>th</sup> to
31<sup>st</sup> July 2026." Don't explain the journal, the `B:`/`BL:` markers,
or the printing habit; that's the machinery behind the post, not its subject.
Once a few of these exist, follow the previous one's opening rather than
inventing a new framing, and say plainly in your reply that the intro is
yours to rewrite.

### 5. Preview it

Build a single-page HTML preview and publish it as an artifact so he can read
the post as a page instead of as a diff. Worth including: the resolved front
matter, a count of books and blogs, every entry rendered, and the `TK` markers
visibly flagged so the remaining work is obvious at a glance. Load the
`artifact-design` skill before writing it.

Redeploy the same file path when he asks for changes so the link stays stable.

### 6. Commit

Commit message must **not** start with `[deploy]` — CI builds but withholds
publishing for unprefixed commits, which is what you want for a draft he
hasn't approved yet. Push to the current branch. Don't touch `docs/`.

## Report back

The post is a draft, not a delivery, so end with what he needs to decide:

- Every `TK` you left, and why
- Anything you read as ambiguous handwriting, with your best guess named
- Any `B:` or `BL:` line you couldn't resolve to a title or a link
- Larger grammar or flow edits you did **not** apply, as before/after pairs
- The fact that the intro is yours

Keep the report to those items. Lines outside `B:` and `BL:` don't belong in
your reply any more than they belong in the post.

Journal page ranges routinely overlap or contradict each other across days —
he is writing quickly, not keeping ledgers. Transcribe what's on the page and
ask, rather than quietly reconciling the numbers.

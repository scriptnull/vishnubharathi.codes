(Wish I started this page earlier. Now, I have to reconcile my years of work - lol)

Legend:
- 🚢 emoji means "production" deployment.
- `*` means current week.

## Week 14, 2026*
(Mar 28 - Apr 3)

- At Work
  - 🏗️ TBD
- [Rho Reader](https://github.com/scriptnull/rho-reader)
  - 🏗️ TBD

## Week 13, 2026
(Mar 21 - Mar 27)

- At Work
  - 🚢 Small backend change related to [PromptQL OLU Pricing](https://promptql.io/pricing).
  - 🚢 Lint fixes needed for Go upgrade in multiple services.
- [Rho Reader](https://github.com/scriptnull/rho-reader)
  - ⏸️ No ship. Intentionally paused this project.

## Week 12, 2026
(Mar 14 - Mar 20)

- At Work
  - 🚢 Shipped a UI change related to [PromptQL OLU Pricing](https://promptql.io/pricing).
  - Went crazy with Claude Code. It helped me create 6 PRs to compare and contrast different UIs for the same functionality.
- [Rho Reader](https://github.com/scriptnull/rho-reader)
  - ⏸️ No ship. Intentionally paused this project.

## Week 11, 2026
(Mar 7 - Mar 13)

- At Work
  - 📲 On-call week.
  - 🤹 Juggling between various items.
- [Rho Reader](https://github.com/scriptnull/rho-reader)
  - ⏸️ No ship. Intentionally paused this project.

## Week 10, 2026
(Feb 28 - Mar 6)

I was down with allergies for most of the week 🤒

## Week 9, 2026
(Feb 21 - Feb 27)

- At Work
  - 📲 On-call week.
  - 😥 Caused an incident. Made mistakes while handling it. Came out strong with some lessons learned from this experience.
  - 🚢 Shipped a few [connector](https://hasura.io/connectors) related changes to support the evolving [PromptQL](https://promptql.io) system.
  - 🚢 Investigated and tweaked Kubernetes configs to enable seamless scale-up/down of a service.
- [Rho Reader](https://github.com/scriptnull/rho-reader)
  - 🤷 No ship.


## Week 8, 2026
(Feb 14 - Feb 20)

- At Work
  - 🚢 Shipped a new API that helped to avoid 50-second latency in the user experience.
- [Rho Reader](https://github.com/scriptnull/rho-reader)
  - 🚢 Released [v0.3.1](https://github.com/scriptnull/rho-reader/releases/tag/v0.3.1)
    - Fixed a bug that has been bugging me for a while 😆

## Week 7, 2026
(Feb 7 - Feb 13)

- At Work
  - Continuing with [Supergraph](https://hasura.io/docs/3.0/project-configuration/supergraph/) build speed up experiement.
  - 🚢 Rolled out infra changes to support my experiment.
- [Rho Reader](https://github.com/scriptnull/rho-reader):
  - 🤷 No ship.


## Week 6, 2026
(Jan 31 - Feb 6)
- At Work
  - Priority shifted and did experiments to improve [Supergraph](https://hasura.io/docs/3.0/project-configuration/supergraph/) build speeds.
- [Rho Reader](https://github.com/scriptnull/rho-reader):
  - 🤷 No ship.

## Week 5, 2026
(Jan 24 - Jan 30)
- At Work:
  - Experimented with making [Hasura/PromptQL connector](https://hasura.io/connectors) deployments faster.
- [Rho Reader](https://github.com/scriptnull/rho-reader):
  - 🚢 Released [v0.3.0](https://github.com/scriptnull/rho-reader/releases/tag/v0.3.0). It contains:
    - OPML Import UI
    - Contextual status message
    - Pulse animation for status bar indicator
    - Bug fixes and tests.

## Week 4, 2026
(Jan 17 - Jan 23)
- At Work:
  - 🚢 Rolled out an optimization that speeds up the deployment of [Hasura/PromptQL connectors](https://hasura.io/connectors). It is 30% to 35% faster.

## Week 3, 2026
(Jan 10 - Jan 16)
- At Work:
  - Finished the draft of a major improvement, but couldn't ship. (pongal holiday + on-call)
  - 🚢 Shipped a few minor improvements that needed immediate attention during on-call duties.

## Week 2, 2026
(Jan 3 - Jan 9)
- At Work:
  - Experimented with Claude Code for the first time 😅. (a bit late to the party).
  - Only had two working days for this week. (travel, team meet, and self-care Friday)
  - 🚢 Pushed a minor change that is part of an upcoming bigger improvement.
  - 🚢 Cleaned up lint and formatting issues across multiple services to stabilize builds.
- [Rho Reader](https://github.com/scriptnull/rho-reader):
  - 🚢 Released [v0.2.0 version](https://github.com/scriptnull/rho-reader/releases/tag/v0.2.0) 🎉. Some things included in this release 👇
    - Import OPML
    - Copy Link button
    - Sync Indicator
    - Mark all as Read button
    - Test Improvements

## Week 1, 2026
(Dec 27 - Jan 2)
- New blog post: [2025: Year in review](https://vishnubharathi.codes/blog/2025-year-in-review)
- At Work:
  - 🚢 Shipped last-mile improvements to the AI Security Agent I’d been working on through Q4 2025.
    - Wider instrumentation across the org.
    - Integrated it with a remote coding agent to deliver automated security fixes.
  - Officially launched the AI Security Agent by announcing it to the entire team on New Year’s Day 🎉
  - Battled with [OTel Context Propagation](https://opentelemetry.io/docs/concepts/context-propagation/) issues across a few services — this one really tripped me up, but was a great learning experience.
- [Rho Reader](https://github.com/scriptnull/rho-reader):
  - 🚢 Released the [first-ever version](https://github.com/scriptnull/rho-reader/releases/tag/v0.1.0) 🎊 Some things included in this release 👇 
    - Browse feeds
    - View unread feeds
    - Add RSS feed
    - Mark as Unread button
  - Added several new features now sitting in `main`, currently under alpha testing in my own Obsidian vault.

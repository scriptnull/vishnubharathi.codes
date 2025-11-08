# [vishnubharathi.codes](https://vishnubharathi.codes) [![](https://github.com/scriptnull/vishnubharathi.codes/workflows/Deployment/badge.svg)](https://vishnubharathi.codes)

Some things about me.

_Framework_: This site is based on [hexo blogging framework](https://hexo.io/).

_Theme_: This site uses a [forked version](https://github.com/scriptnull/hexo-theme-cactus) of the [cactus theme for hexo](https://github.com/probberechts/hexo-theme-cactus).

## Development:

This website is deployed via Github Actions. To start an automated deployment for your commit, start the commit message with `[deploy]`.

Following instructions apply for local development environment (which could be used for things like patching the theme etc.)

- Install node.js and npm - https://nodejs.org/en/
- Run `npm i`.
- clone the [theme](https://github.com/scriptnull/hexo-theme-cactus) to themes/cactus folder.
  ```sh
  git clone git@github.com:scriptnull/hexo-theme-cactus.git
  ```
- Make changes and run `npm run dev`. Visit http://localhost:4000
- To publish all the work, run `./package.sh`. git commit and push to this repository.

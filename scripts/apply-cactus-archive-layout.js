'use strict';

const fs = require('fs');
const path = require('path');

// Tag pages render through themes/cactus/layout/archive.ejs, which also renders
// the blog archives. CI reclones the theme, so the single-tag heading is kept
// in theme-overrides and swapped in after that clone.
hexo.extend.filter.register('before_generate', function () {
  const override = path.join(hexo.base_dir, 'theme-overrides/cactus/layout/archive.ejs');
  hexo.theme.setView('archive.ejs', fs.readFileSync(override, 'utf8'));
});

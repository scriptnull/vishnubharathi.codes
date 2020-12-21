#!/bin/bash -e

npx hexo version
npx hexo generate
rm -rf ./docs
mv public ./docs
cp ./CNAME ./docs/CNAME

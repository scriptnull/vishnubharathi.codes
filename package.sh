#!/bin/bash -e

npx hexo generate
rm -rf ./docs
mv public ./docs
cp ./CNAME ./docs/CNAME

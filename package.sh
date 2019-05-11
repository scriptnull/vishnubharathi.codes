#!/bin/bash -e

./node_modules/.bin/hexo generate
rm -rf ./docs
mv public ./docs
cp ./CNAME ./docs/CNAME

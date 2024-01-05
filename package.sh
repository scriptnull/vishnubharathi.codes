#!/bin/bash -e

npx hexo version
npx hexo generate
rm -rf ./docs
mv public ./docs
cp ./CNAME ./docs/CNAME
mkdir -p ./docs/.well-known
cp  ./source/.well-known/atproto-did ./docs/.well-known/atproto-did

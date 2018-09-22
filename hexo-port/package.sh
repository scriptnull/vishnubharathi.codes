#!/bin/bash -e

hexo generate
rm -rf ../docs
mv public ../docs
cp ../CNAME ../docs/CNAME

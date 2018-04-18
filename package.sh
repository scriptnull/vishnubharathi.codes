#!/bin/bash -e

hugo
rm -rf docs
mv public docs
cp CNAME docs/CNAME

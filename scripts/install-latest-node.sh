#!/usr/bin/env bash

nodeVersion=$(curl https://resolve-node.now.sh/)

wget "http://nodejs.org/dist/${nodeVersion}/node-${nodeVersion}-linux-x64.tar.gz" \
    -O latest-node.tar.gz

tar -xzf latest-node.tar.gz \
    --exclude CHANGELOG.md \
    --exclude LICENSE \
    --exclude README.md \
    --strip-components 1 \
    -C /usr/local

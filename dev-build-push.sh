#!/usr/bin/env bash

if [ ! -f scale-ui/deploy/scale-ui-master.tar.gz ]
then
    cd scale-ui
    tar xf node_modules.tar.gz
    tar xf bower_components.tar.gz
    npm install
    node node_modules/gulp/bin/gulp.js deploy
    cd ..
fi

docker build -t $1 -f Dockerfile-dev .
docker push $1

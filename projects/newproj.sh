#!/bin/bash

mkdir "$1"
cd "$1"
cp -r ../template/* .
cd ..
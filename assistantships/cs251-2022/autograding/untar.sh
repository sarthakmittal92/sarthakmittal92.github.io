#!/bin/bash

mkdir submissions
for d in ./zips/*
do
    cp $d/*.gz submissions
done
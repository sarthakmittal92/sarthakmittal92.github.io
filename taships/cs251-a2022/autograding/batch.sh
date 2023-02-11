#!/bin/bash

touch marks.txt
while read -r line
do
    ./autograde.sh $line
done < rolls.txt
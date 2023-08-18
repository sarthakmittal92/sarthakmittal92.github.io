#!/bin/bash

# Specify the directory to iterate over
directory="submission"

if [ "$#" -lt 1 ]; then
    echo "Give roll number"
    exit
fi

rollno="$1"
cd $directory
mkdir -p $rollno
cd $rollno
cp -r ../../* .
tar -xf ../$rollno@iitb.ac.in.tar.gz
cd ../..

# Check if the directory exists
if [ -d "$directory" ]; then
    for folder in "$directory"/*; do
        # Check if the current item is a directory
        if [ -d "$folder" ]; then
            cd $folder
            python3 script.py
            cd ..
            rm -f evaluate.json
        fi
    done
else
    echo "Directory does not exist: $directory"
fi

rm -rf $rollno

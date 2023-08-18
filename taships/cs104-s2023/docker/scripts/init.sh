#!/bin/bash

sudo docker run --name "$1" -it --net=host --env="DISPLAY" -v "$HOME:/host" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" d080da90d685
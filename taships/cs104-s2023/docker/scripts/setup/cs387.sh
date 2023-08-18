#!/bin/bash

# works for Linux (X86-64/AMD64 Architecture)
# enter 'cse_user' and 'user_auth_pass' on prompt

sudo docker login docker.cse.iitb.ac.in
sudo docker pull docker.cse.iitb.ac.in/cs387
xhost +
echo "You're all set now!"
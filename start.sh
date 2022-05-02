#!/bin/bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/docker_key
git clone git@github.com:carnet98/AST-Project-Carnet-Neffj.git
cd AST-Project-Carnet-Neffj
git checkout -b Colin
git pull origin Colin
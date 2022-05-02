#!/bin/bash
cd AST-Project-Carnet-Neffj
MESSAGE=${1:?"missing arg 1 for commit message, please retry with a commit message"}
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/docker_key
git add .
git commit -m "$1"
git push --set-upstream origin Colin
exit

#!/usr/bin/env bash
set -e
REPO_URL=${1:-""}
if [ -z "$REPO_URL" ]; then
  echo "Usage: bash push_to_github.sh <https-repo-url>"
  exit 1
fi
git init
git branch -M main
git add .
git commit -m "Initial commit: S225 HIT137 Assignment 2 (S1 2025)"
if git remote | grep -q origin; then
  git remote set-url origin "$REPO_URL"
else
  git remote add origin "$REPO_URL"
fi
git push -u origin main
echo "Pushed to $REPO_URL"

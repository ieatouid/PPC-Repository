
#!/bin/bash

FREQ_RESULT="$1"
GITHUB_USER="$2"

TIMESTAMP=$(date)

echo -e "\n### Vowel Frequency Update\nContributor: $GITHUB_USER\nResults: $FREQ_RESULT\nUpdated: $TIMESTAMP" >> README.md

git config --global user.name "github-actions"
git config --global user.email "github-actions@users.noreply.github.com"
git config --global --add safe.directory /app

git add README.md
git commit -m "Update README with vowel frequency results" || echo "No changes to commit"

git remote set-url origin "https://x-access-token:${GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}.git"

git fetch origin main

git rebase origin/main

git push origin HEAD:main


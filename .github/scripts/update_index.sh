
#!/bin/bash

# Receive the two input files
TASK_FILE="$1"
TEST_FILE="$2"

# Extract the ToDo tasks
TODO_TASKS=$(awk '
    /^ToDo Tasks:/ {flag=1; next}
    /^Done Tasks:/ {flag=0}
    flag
' "$TASK_FILE")

# Extract the completed tasks
DONE_TASKS=$(awk '
    /^Done Tasks:/ {flag=1; next}
    flag
' "$TASK_FILE")

# Read the unit test results
TEST_RESULTS=$(cat "$TEST_FILE")

# Function to update a pre element in index.html
update_pre() {
    PRE_ID="$1"
    CONTENT="$2"

    export CONTENT

    perl -0777 -i -pe \
    "s{(<pre id=\"$PRE_ID\">).*?(</pre>)}{\$1\$ENV{CONTENT}\$2}s" \
    /app/index.html
}

# Update the three HTML sections
update_pre "todo-tasks" "$TODO_TASKS"
update_pre "done-tasks" "$DONE_TASKS"
update_pre "test-results" "$TEST_RESULTS"

# Configure Git
git config --global user.name "github-actions[bot]"
git config --global user.email "41898282+github-actions[bot]@users.noreply.github.com"
git config --global --add safe.directory /app

# Add the updated HTML file
git add /app/index.html

# Commit the changes
git commit -m "Update index.html with task manager results" || echo "No changes to commit"

# Configure remote authentication
git remote set-url origin "https://x-access-token:${GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}.git"

# Synchronise with GitHub
git fetch origin main
git rebase origin/main

# Push changes
git push origin HEAD:main


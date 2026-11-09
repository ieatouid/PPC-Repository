
#!/bin/bash

# Stop if an error occurs
set -e
set -o pipefail

echo "Starting Task Manager..."

# Run the task management application
python3 /app/.github/scripts/todo.py | tee /app/task-output.txt

# Run the unit tests
python3 /app/.github/scripts/todo-test.py | tee /app/test-output.txt

# Update the HTML file
bash /app/.github/scripts/update_index.sh \
    /app/task-output.txt \
    /app/test-output.txt

echo "Task Manager Process Completed!"

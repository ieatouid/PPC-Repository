
#!/bin/bash

set -e

echo "Starting Frequency Analyzer..."

FREQ_RESULT=$(python3 /app/.github/scripts/frequency.py /app/${FILE:-data.txt})

bash /app/.github/scripts/update_readme.sh "$FREQ_RESULT" "$GITHUB_USER"

echo "Process Completed!"

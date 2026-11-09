
# Use Python as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install Git, Perl and required utilities
RUN apt-get update && \
    apt-get install -y git perl gawk && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy repository files into the container
COPY . /app

# Make shell scripts executable
RUN chmod +x /app/.github/scripts/entrypoint.sh && \
    chmod +x /app/.github/scripts/update_index.sh

# Start the entrypoint script
ENTRYPOINT ["/bin/bash", "/app/.github/scripts/entrypoint.sh"]

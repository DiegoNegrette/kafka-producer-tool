FROM docker.redpanda.com/redpandadata/redpanda:latest

# Switch to root to install packages
USER root

# Install rpk CLI using official method
RUN apt-get update && apt-get install -y redpanda

# Verify rpk installation
RUN rpk version

# Switch back to the default user for security
USER redpanda




# Start from Python 3.8.5 slim-buster image
FROM python:3.8.5-slim-buster

# Set the environment variable to prevent caching in pip
ENV PIP_NO_CACHE_DIR 1

# Remove default AWS mirror (if needed)
RUN sed -i.bak 's/us-west-2\.ec2\.//' /etc/apt/sources.list

# Upgrade pip and setuptools
RUN pip3 install --upgrade pip setuptools

# Copy local files into the container
COPY . /root/Data-hrame.bot

# Set the working directory inside the container
WORKDIR /root/Data-hrame.bot

# Install Python requirements from requirements.txt
RUN pip3 install -U -r requirements.txt

# Copy the entrypoint script and make it executable
COPY entrypoint.sh /root/entrypoint.sh
RUN chmod +x /root/entrypoint.sh

# Set the entry point for the container
ENTRYPOINT ["/root/entrypoint.sh"]

# Optional: Expose a port if your bot communicates through a webhook or API
# EXPOSE 80

# Command to run the bot (this will be overridden by entrypoint.sh if needed)
CMD ["python", "bot.py"]


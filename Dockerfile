FROM python:3.8.5-slim-buster

# Update apt sources
RUN sed -i.bak 's/us-west-2\.ec2\.//' /etc/apt/sources.list

# Upgrade pip and setuptools
RUN pip3 install --upgrade pip setuptools

# Copy the application files
COPY . /root/Waifubot-

COPY main /opt/render/project/src/main

# Set the working directory
WORKDIR /root/Waifubot-

# Install dependencies
RUN pip3 install -U -r requirements.txt

# Copy entrypoint script and make it executable
COPY entrypoint.sh /root/entrypoint.sh
RUN chmod +x /root/entrypoint.sh

# Set the entrypoint for the container
ENTRYPOINT ["/root/entrypoint.sh"]





From python:3.8.5-slim-buster

ENV PIP_NO_CACHE_DIR 1

RUN sed -i.bak 's/us-west-2\.ec2\.//' /etc/apt/sources.list

#Upgrade pip and setuptools
RUN pip3 install --upgrade pip  setuptools

#Copy local files to the container
COPY . /root/Data-hrame.bot
-
WORKDIR /Data-hrame.bot
t-


#Install python requrements
RUN pip3 insatll -U -r requirements.txt

#Copy the entrypoint script and make it executable
COPY entrypoint.sh /root/entrypoint.sh
RUN chmod +x /root/entrypoint.sh


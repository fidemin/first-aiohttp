FROM python:3.7.3
RUN apt-get -y update
RUN apt-get install -y git
WORKDIR /home/yhmin/
RUN git clone https://github.com/yhmin84/first-aiohttp
WORKDIR /home/yhmin/first-aiohttp
RUN pip3 install -r requirements.txt
RUN mkdir config
COPY ./config/docker.config.yaml config/config.yaml
CMD git pull && ./bin/entrypoint.sh

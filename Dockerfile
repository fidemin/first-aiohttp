FROM centos:centos7
RUN yum -y update && yum install -y epel-release

# python 설치
RUN yum install -y gcc openssl-devel bzip2-devel libffi-devel make
WORKDIR /usr/src
COPY ./Python-3.7.3.tgz  .
RUN tar xzf Python-3.7.3.tgz
RUN rm Python-3.7.3.tgz
WORKDIR Python-3.7.3
RUN ./configure --enable-optimizations
RUN make altinstall
RUN python3.7 -V
WORKDIR /usr/local/bin
RUN ln -s python3.7 python3
RUN ln -s pip3.7 pip3

RUN yum install -y git
WORKDIR /home/yhmin/
RUN git clone https://github.com/yhmin84/first-aiohttp
WORKDIR /home/yhmin/first-aiohttp
RUN mkdir config
COPY ./config/docker.config.yaml config/config.yaml
RUN pip3 install -r requirements.txt
CMD ["python3.7", "server/main.py", "--config=config/config.yaml"]

FROM alpine
MAINTAINER Andrew Dunai <a@dun.ai>

RUN apk add --update
RUN apk add python3 python3-dev py-pip
RUN apk add bash

RUN mkdir /root/dunai
WORKDIR /root/dunai

COPY requirements.txt /root/dunai

RUN pip3.6 install -r ./requirements.txt

COPY manage.py /root/dunai
COPY dunai /root/dunai/dunai

CMD ["bash"]


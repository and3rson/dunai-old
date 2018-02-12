FROM alpine
MAINTAINER Andrew Dunai <a@dun.ai>

RUN apk update
RUN apk add --update
RUN apk add python3 python3-dev py-pip libjpeg
RUN apk add bash
RUN apk add py3-pillow
RUN apk add py3-psycopg2
RUN apk add py3-lxml libxml2

RUN mkdir /root/dunai
WORKDIR /root/dunai

COPY requirements.txt /root/dunai

RUN pip3.6 install -r ./requirements.txt

COPY manage.py /root/dunai
COPY dunai /root/dunai/dunai

CMD ["bash"]


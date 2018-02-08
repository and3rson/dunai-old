FROM alpine
MAINTAINER Andrew Dunai <a@dun.ai>

RUN apk update
RUN apk add --update
RUN apk add python3 python3-dev py-pip libjpeg
RUN apk add bash
RUN apk add py3-pillow
RUN apk add py3-psycopg2
RUN wget http://dl-3.alpinelinux.org/alpine/edge/testing/x86_64/wkhtmltopdf-0.12.4-r0.apk -O /tmp/wkhtmltopdf.apk
RUN apk add wkhtmltopdf.apk

RUN mkdir /root/dunai
WORKDIR /root/dunai

COPY requirements.txt /root/dunai

RUN pip3.6 install -r ./requirements.txt

COPY manage.py /root/dunai
COPY dunai /root/dunai/dunai

CMD ["bash"]


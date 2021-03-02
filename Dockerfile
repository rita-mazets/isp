FROM python:3.6

RUN mkdir -p /usr/src/laba1/

WORKDIR  /usr/src/laba1/

COPY . /usr/src/laba1/

CMD ["python3", "laba1.py"]

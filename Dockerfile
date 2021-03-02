FROM python:3.6

RUN mkdir -p /usr/src/labaa1/

WORKDIR  /usr/src/labaa1/

COPY . /usr/src/labaa1/

RUN set -ex \ pip3 install —no-cache-dir -r requirements.txt \
&& rm requirements.txt

CMD ["python3", "laba1.py"]

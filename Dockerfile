FROM python:3.9-slim

WORKDIR /MS

COPY ./requirements.txt /MS
COPY ./main.py /MS
COPY ./test_main.py /MS

RUN	pip3 install --upgrade pip
RUN	pip3 install -r requirements.txt

ENTRYPOINT python main.py

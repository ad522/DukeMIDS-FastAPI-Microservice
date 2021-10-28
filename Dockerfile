FROM python:3.9-slim

WORKDIR /MS

COPY ./requirements.txt /MS
COPY ./main.py /MS
COPY ./test_main.py /MS

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT python main.py

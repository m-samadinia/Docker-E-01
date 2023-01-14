FROM python:3.7-slim

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . /code/

ENV DEFAULT_PORT=8080

CMD ["python", "main.py"]


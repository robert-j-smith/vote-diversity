FROM python:alpine3.7

COPY requirements.txt /

RUN pip install -r requirements.txt

COPY vote.py /

ENTRYPOINT ["python", "/vote.py"]

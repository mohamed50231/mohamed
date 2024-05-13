FROM python:alpine

WORKDIR /assignment4

COPY . .

RUN pip install NLTK

CMD ["python", "script.py"]
FROM python:2.7

ENV PYTHONUNBUFFERED 1
ENV django_dir /django

RUN mkdir $django_dir
WORKDIR $django_dir
COPY ./* ./
RUN pip install -r requirements.txt

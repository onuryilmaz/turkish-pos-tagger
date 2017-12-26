FROM python:2.7.11

COPY . /turkish-pos-tagger
WORKDIR /turkish-pos-tagger

RUN pip install pyyaml
RUN pip install -U nltk

RUN python training_tagger.py
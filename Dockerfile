FROM python:3.7.7-slim-buster
LABEL maintainer="hp5588@gmail.com"

EXPOSE 8000

RUN mkdir cv-site
COPY . ./cv-site
WORKDIR ./cv-site
RUN pip install .

ENTRYPOINT ["/bin/bash", "/cv-site/entrypoint.sh"]


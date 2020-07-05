FROM python:3.7.7-slim-buster

ENV ENV_STATIC_URL https://static.po-wen.de/cv/static/
EXPOSE 8000

#  for testing
RUN mkdir cv-site
COPY . ./cv-site
#RUN git pull
WORKDIR ./cv-site

#RUN mkdir data
#RUN chmod +x entrypoint.sh
RUN pip install .

ENTRYPOINT ["/bin/bash", "/cv-site/entrypoint.sh"]


FROM python:3.9.2-slim-buster

RUN pip3 install -r requirements.txt

CMD ["bash","start.sh"]

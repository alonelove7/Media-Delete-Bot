FROM python:3.9.2-slim-buster

COPY . .

WORKDIR /app

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["bash","start.sh"]

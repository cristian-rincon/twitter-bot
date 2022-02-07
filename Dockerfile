FROM python:3.8-alpine

WORKDIR /bot
COPY ./bot/ /bot/
RUN pip install tweepy

CMD ["python", "/bot/main.py"]

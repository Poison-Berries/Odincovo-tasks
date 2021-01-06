FROM python:3.9-alpine3.12

COPY requirements.txt /
RUN ["pip3", "install", "-r", "/requirements.txt"]

COPY task/ /task

WORKDIR /task
EXPOSE 5000

CMD ["python3", "server.py"]

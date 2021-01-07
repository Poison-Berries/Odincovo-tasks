FROM python:3.8.5

COPY requirements.txt /requirements.txt
RUN ["pip3", "install", "-Ur", "/requirements.txt"]

COPY task_source/ /app
EXPOSE 5091
WORKDIR /app
CMD ["python3", "webserver.py"]

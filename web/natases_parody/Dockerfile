FROM python:3.9.1-alpine3.12

COPY task_source/ /static/

EXPOSE 8000

CMD ["python3", "-m", "http.server", "--directory", "/static"]

FROM python:3.9.1-alpine3.12 AS py-prepare

WORKDIR /app
COPY task_source/prepare_task.py /app/
RUN ["python3", "prepare_task.py"]
RUN rm prepare_task.py

FROM ubuntu:20.04

RUN ["apt", "update"] # To make `apt install` easier

COPY --from=py-prepare /app/Test-ground /Test-ground
WORKDIR /Test-ground

CMD ["/bin/bash"]

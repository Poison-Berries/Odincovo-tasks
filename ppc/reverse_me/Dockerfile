FROM python:3.9.1

RUN apt update && apt install ncat --assume-yes

WORKDIR /app

COPY task_source/dictionary.txt task_source/listener.py ./

EXPOSE 4444

CMD ["bash", "-c", "for((;;)); do ncat -kl 4444 -e listener.py; done"]

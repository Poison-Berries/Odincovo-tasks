FROM python:3.9.1

RUN apt update && apt install ncat --assume-yes

WORKDIR /app

COPY dictionary.txt ./
COPY listener.py ./

EXPOSE 4444

CMD ["ncat", "-kl", "4444", "-e", "listener.py"]

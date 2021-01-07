#!/usr/bin/python3
from random import choice
from time import time


with open("dictionary.txt", "r") as f:
    words = f.read().split()


def main():
    print("HellooooOoOoOoO! So glad to see you here :). Help me 500 times")
    print("Let's begin. Do you know, what these words are? 😳")
    for i in range(500):
        word = choice(words)
        rev = word[::-1]
        start = time()
        print("Try this one:", rev)
        if input() != word:
            print("Incorrect. You are LOH.")
            exit(0)
        elif time() - start > 2:
            print("https://music.yandex.ru/album/4436941/track/35540581")
            exit(0)
        else:
            print("Cool! Keep going...")

    print("Your flag is PB{Plumbum}")


if __name__ == '__main__':
    try:
        main()
    except:
        exit(0)

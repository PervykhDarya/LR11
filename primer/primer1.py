#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from threading import Thread
from time import sleep


def func():
    for i in range(5):
        print(f"from child thread: {i}")
        sleep(0.5)


if __name__ == '__main__':
    th = Thread(target=func)
    th.start()

    for i in range(5):
        print(f"from main thread: {i}")
    sleep(1)
with open("data.txt", "w") as f:
    f.write("Hello Ahad")

class Transaction:
    def __enter__(self):
        print("Starting transaction")
        return self  # you usually return the DB connection

    def __exit__(self, exc_type, exc, trace):
        if exc_type:
            print("Error happened. Rolling back transaction.")
        else:
            print("Committing transaction.")

with Transaction() as t:
    print("Buying item…")

import threading

lock = threading.Lock()

with lock:
    # critical section
    print("Lock acquired. Doing work...")

import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self  # return self so we can access timer.elapsed

    def __exit__(self, *args):
        self.end = time.time()
        self.elapsed = self.end - self.start

with Timer() as t:
    sum([i for i in range(1000000)])

print(f"Took {t.elapsed} seconds")

import os

class ChangeDir:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.original = os.getcwd()
        os.chdir(self.path)
        return self

    def __exit__(self, *args):
        os.chdir(self.original)

print("Before:", os.getcwd())

with ChangeDir("/tmp"):
    print("Inside:", os.getcwd())

print("After:", os.getcwd())

import requests

with requests.Session() as s:
    response = s.get("https://example.com")
    print(response.status_code)

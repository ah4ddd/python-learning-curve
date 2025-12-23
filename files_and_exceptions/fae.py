from contextlib import contextmanager

@contextmanager
def db_connection():
    print("🔌 connect")
    try:
        yield "DB"
    finally:
        print("🔌 close")

db_connection()

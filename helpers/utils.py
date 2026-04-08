import time
from contextlib import ContextDecorator


class timer(ContextDecorator):
    def __init__(self, label="Block"):
        self.label = label

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *exc):
        self.end = time.perf_counter()
        print(f"{self.label} took: {self.end - self.start:.6f} seconds")
        return False

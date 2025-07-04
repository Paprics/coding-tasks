import multiprocessing
from datetime import time
from random import random


def timer():
    start = time.time()
    yield
    print(f"Elapsed: {time.time() - start:.2f} seconds")



DATA_SIZE = 10_000_000
lst = []
workers = 1

def fill_data(n):
    while n > 0:
        n -= 1
        lst.append(random.randint(1, 100))

with timer(f"Elapsed: {}s"):
    with multiprocessing.Pool(workers) as pool:
        input_data = [DATA_SIZE // workers for _ in range(workers)]
        pool.map(fill_data, input_data)

print(len(lst), lst[:100])
import os
import string
import random
import requests
from concurrent.futures import ThreadPoolExecutor
import time

def fetch_pic(num_pic):
    url = 'https://picsum.photos/400/600'
    path = os.path.join(os.getcwd(), 'img')
    os.makedirs(path, exist_ok=True)

    for _ in range(num_pic):
        random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        response = requests.get(url)
        if response.status_code == 200:
            with open(f'{path}/{random_name}.jpg', 'wb') as f:
                f.write(response.content)

def timer():
    start = time.time()
    yield
    print(f"Elapsed: {time.time() - start:.2f} seconds")

if __name__ == '__main__':
    workers = 128
    total_pics = 100
    pics_per_worker = total_pics // workers

    start = time.time()
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(fetch_pic, pics_per_worker) for _ in range(workers)]
        for future in futures:
            future.result()

    print(f"Elapsed: {time.time() - start:.2f} seconds")

# 1 - 100 - 110
# 2 - 100 - 84
# 4 - 100 - 49
# 8 - 100 - 15
# 16 - 100 - 10
# 32 - 100 - 6
# 64 - 100 - 8


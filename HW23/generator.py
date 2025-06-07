import requests

def word_generator(quantity):
    if not isinstance(quantity, int):
        raise TypeError('quantity must be an integer')

    if quantity > 10000:
        quantity = 10000

    response = requests.get(f'https://random-word-api.herokuapp.com/word?number={quantity}')
    if response.status_code != 200:
        raise ConnectionError('Request failed')

    yield from response.json()

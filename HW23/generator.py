import requests

def word_generator(quantity, max_words=10000):
    words = set()

    while len(words) < quantity and len(words) < max_words:
        response = requests.get('https://random-word-api.herokuapp.com/word')
        if response.status_code != 200:
            raise ConnectionError('Request failed')

        word = response.json()[0]
        if word not in words:
            words.add(word)
            yield word

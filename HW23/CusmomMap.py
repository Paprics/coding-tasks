class MapCustom_one:
    """Iteration state via list index"""

    def __init__(self, dictionary, func_one, func_two):
        self.dictionary = self._dict_validator(dictionary)
        self.func_one = self._func_validator(func_one)
        self.func_two = self._func_validator(func_two)
        self.list_keys = list(self.dictionary.keys())
        self.length = len(self.list_keys)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.length:
            raise StopIteration

        key = self.list_keys[self.index]
        value = self.dictionary.get(key)
        self.index += 1
        return self.func_one(key), self.func_two(value)

    def _dict_validator(self, dictionary):
        if not isinstance(dictionary, dict):
            raise TypeError('Object must be a dictionary')
        return dictionary

    def _func_validator(self, func):
        if not callable(func):
            raise TypeError('Object must be a function')
        return func


class MapCustom_two(MapCustom_one):
    """Iteration state via dict iterator """

    def __init__(self, dictionary, func_one, func_two):
        super().__init__(dictionary, func_one, func_two)
        self._iterator = iter(self.dictionary.items())

    def __next__(self):
        key, value = next(self._iterator)
        return self.func_one(key), self.func_two(value)

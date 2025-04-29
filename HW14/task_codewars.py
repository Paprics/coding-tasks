def mirror(text, mirror_chars=None):
    #https://www.codewars.com/kata/571af500196bb01cc70014fa

    text = text.lower()

    if mirror_chars is None:
        mirror_chars = 'abcdefghijklmnopqrstuvwxyz'

    mirror_chars = mirror_chars.lower()
    reversed_chars = mirror_chars[::-1]

    result = ""
    for c in text:
        if c in mirror_chars:
            result += reversed_chars[mirror_chars.index(c)]
        else:
            result += c

    return result


print(mirror("Welcome home"))
print(mirror("hello", "abcdefgh"))


def decode(message):
    #https://www.codewars.com/kata/565b9d6f8139573819000056
    mirror = {
        'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's',
        'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k',
        'q': 'j', 'r': 'i', 's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c',
        'y': 'b', 'z': 'a'
    }

    result = ""

    for char in message:
        if char == ' ':
            result += ' '
        else:
            result += mirror[char]

    return result


print(decode("r slkv mlylwb wvxlwvh gsrh nvhhztv"))

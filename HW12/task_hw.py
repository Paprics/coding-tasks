def new_format(s):
    s = s[::-1]
    parts = []
    for i in range(0, len(s), 3):
        parts.append(s[i:i+3])
    return ".".join(part[::-1] for part in parts[::-1])

assert (new_format("1000000") == "1.000.000")
assert (new_format("100") == "100")
assert (new_format("1000") == "1.000")
assert (new_format("100000") == "100.000")
assert (new_format("10000") == "10.000")
assert (new_format("0") == "0")
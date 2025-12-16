from collections import Counter

letters = Counter({"i": 4, "s": 4, "p": 2, "m": 1})

# argument type 1
letters.update("missouri")
print(letters)

# argument type 2
letters.update({"i":1})
print(letters)
letters.update({"i":2})
print(letters)
dictionary = {}

array = ['one', 'two', 'three', 'dour', 'five']

for _ in array:
    dictionary[_] = 4

for _ in dictionary:
    if dictionary[_] == 4:
        dictionary[_] += 170

print(dictionary)
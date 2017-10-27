import random

'''
num_list = []
count = 0

while count < 10:
    num = random.randint(0, 10)
    if num not in num_list:
        num_list.append(num)
        count += 1

print(num_list)
'''

with open('/usr/share/dict/words', 'r') as f:
    all_words = f.readlines()
    print(all_words)
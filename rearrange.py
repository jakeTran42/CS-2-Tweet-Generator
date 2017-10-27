import random
import sys

# words = ['time', 'space', 'antimatter', 'universe', 'neutron']
words = sys.argv[1:]

def create_random_quote():
    word = []
    num_already_used = []
    counter = 0
    while counter < len(words):
        rand_index = random.randint(0, len(words) - 1)
        if rand_index not in num_already_used:
            word.append(words[rand_index])
            num_already_used.append(rand_index)
            counter += 1
    return word

if __name__ == '__main__':
    quote = create_random_quote()
    # quote = ' '.join(quote)
    print(quote)
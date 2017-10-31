# import random

# def dictionary(num):
#     with open('/usr/share/dict/words', 'w') as f:
        
import random
import sys

def generate_random_sentence(input_number):
    with open('/usr/share/dict/words', 'r') as f:
        number_of_words = input_number
        # sentence = []
        all_words = f.readlines()
        all_words_array = list(all_words)
        output = []
        for index in all_words_array:
            word = index.replace('\n', '')
            output.append(word)

        sentence_array = []
        for index in range(int(number_of_words)):
            rand_num = random.randint(0, len(output) - 1)
            sentence_array.append(output[rand_num])

        sentence = ' '.join(sentence_array)



        return sentence

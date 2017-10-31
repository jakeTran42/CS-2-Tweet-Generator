import random
import sys


def dictionary(input):
    with open("/usr/share/dict/words", 'r') as f:
        #Reading files and creating a list
        read_text = f.read()
        dictionary_list = list(read_text.split("\n"))

    num_of_word = input

    sentence_list = []

    #Loop through input of num + append random word to a list/array called sentence_list
    for index in range(int(num_of_word)):
        word_index = random.randint(0, len(dictionary_list) - 1)
        sentence_list.append(dictionary_list[word_index])
    
    return sentence_list



if __name__ == '__main__':
    user_input = sys.argv[1:]
    # new_input = int(user_input)
    sentence = dictionary(int(user_input[0])
    print(sentence)
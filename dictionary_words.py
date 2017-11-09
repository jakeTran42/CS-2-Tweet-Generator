import random
import sys
import time


def open_word(filename):
    with open(filename, 'r') as f:
        read_text = f.read()
        dictionary_list = list(read_text.split("\n"))
    return dictionary_list



def dictionary(input, word_list_array):
    # with open("/usr/share/dict/words", 'r') as f:
    #     #Reading files and creating a list
    #     read_text = f.read()
    #     dictionary_list = list(read_text.split("\n"))
    num_of_word = input

    sentence_list = []
    #Loop through input of num + append random word to a list/array called sentence_list
    for _ in range(int(num_of_word)):
        word_index = random.randint(0, len(word_list_array) - 1)
        sentence_list.append(word_list_array[word_index])
    return sentence_list




if __name__ == '__main__':
    starting_time = time.time()
    word_list_array = open_word("/usr/share/dict/words")
    input = int(sys.argv[1])
    for _ in range(10):
        sentence = dictionary(input, word_list_array)
        complete_sentence = ' '.join(sentence)
        print(complete_sentence)
    time_end = time.time()

    print("Time Stamp: " + str(starting_time) + " seconds - " + str(time_end) + " seconds")
    print("Total Time: " + str(time_end - starting_time))

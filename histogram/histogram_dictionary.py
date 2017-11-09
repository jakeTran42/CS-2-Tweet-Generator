'''Histogram'''

def opening_text(filename):
    with open (filename, 'r') as f:
        read_text = f.read()
        clean_text = read_text.replace('.', '').replace(',', '')
        return clean_text

def histogram_dictionary(text_file):
    histogram = {}
    text = text_file.split(" ")
    for word in text:
        word = word.lower()
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram

def frequency_dict(histogram_dict, key_word):
    return histogram_dict[key_word]

def histogram_nested_lists(source_text):
    """Return nested lists of words and frequecy."""
    source_text = source_text.lower()
    text = source_text.split(" ")
    histogram = []
    for word in text:
        create_new_entry = True
        for entry in histogram:
            if entry[0] == word:
                entry[1] += 1
                create_new_entry = False
                break

        if create_new_entry:
            histogram.append([word, 1])
    return histogram

def unique_words(histogram):
    """Return number of unique_words in histogram."""
    return len(histogram)

# def histogram_list_tuples(source_text):
#     """Return a list of tuples."""
#     source_text = source_text.lower()
#     text = source_text.split(" ")
#     histogram = []

#     for word in text:
#         create_new_entry = True
#         for entry in histogram:
#             if entry[0] == word:
#                 num = entry[1] + 1
#                 histogram.remove(entry)
#                 histogram.append((word, num))
#                 create_new_entry = False
#                 break

#         if create_new_entry:
#             histogram.append((word, 1))
#     return histogram





















file_text = opening_text('text.txt')
# file_text2 = histogram_dictionary(file_text)
# file_text3 = histogram_nested_lists(file_text)
file_text4 = histogram_list_tuples(file_text)
# frequecyDict = frequency_dict(file_text2, 'idk')
uniqueWords = unique_words(file_text4)
# print(file_text)
# print(file_text2)
# print(file_text3)
# print(file_text2)
# print(frequecyDict)
print(file_text4)
print(uniqueWords)

text = "hello class how are you"
words = text.split()
#["hello", "class", "how", .....]

new_words = sorted(words) #does not change words

words.sort() #changes words, if you assign it to a new variable then it will return 
            #None bc words.sort() does not take in arguement.


print(new_words)
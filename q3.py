# Read "romeo_and_juliet.txt" (The full text of Shakespeare's Romeo and Juliet)
import re
####
#### YOUR CODE HERE 
####
def original_assighment():
    total = 0

    with open("romeo_and_juliet.txt", "r") as f:
        for line in f:
            total += line.count("juliet")

    print(total)
# Count how many times the word "Juliet" appears

####
#### YOUR CODE HERE 
####
def extension():
    words = {}

    with open("romeo_and_juliet.txt", "r") as f:
        for line in f:
            for word in line.split(" "):
                if word in words:
                    words[word] += 1
                else:
                    words[word] = 1

    #for word in words:
        #if words[word] > 100:
            #print(word, words[word])

    myKeys = list(words.keys())
    myKeys.sort()

    print(words)


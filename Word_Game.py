# THIS IS A TEST
# FOR GITHUB

import random

## Initializes the game elements
# Retrieves the word dictionary
f = open('words.txt', 'r')
text = f.read()

# Splits dictionary & initializes arrays
lines = text.split("\n")
words = []
four_letter_words = []

# Collects all words
for each in lines:
    words += each.split(" ")

# Retrieves only valid 4 letter words
for each in words:
    if len(each) == 4:
        if('-' in each or '.' in each):
            continue
        else:
            four_letter_words.append(each)

four_letter_words = [x.lower() for x in four_letter_words]

########################################
# Gets a random, valid, 4 letter word
def randomword(words):
    word = words[random.randint(0,len(words))]
    return word

###########################################
# Verifies the input has 4 letters
def fourletters(input_word):
    if(len(input_word) != 4):
        return False
    else:
        return True
###########################################
# Verifies there is only 1 difference in the input word
def differences(input_word, prev_word):
    diff = 0
    counter = 0

    while(counter < 4):
        if(input_word[counter] != prev_word[counter]):
            diff = diff + 1

        counter = counter + 1

    if(diff > 1):
        return False
    else:
        return True
##########################################
# Verifies the input is valid
def dictionarycheck(input_word, dictionary):
    verified = False
    for each in dictionary:
        if(input_word == each):
            verified = True

    return verified
###########################################
# Handles gameplay
def gameplay(prev_word, final_word, dictionary):
    input_word = input("Please enter a word: ")
    if(fourletters(input_word) == False):
        print("Please enter a valid word" + '\n')
        print("Previous word was: " +  prev_word)
        gameplay(prev_word, final_word, dictionary)

    if(differences(input_word, prev_word) == False):
        print("Please enter a valid word" + '\n')
        print("Previous word was: " +  prev_word)
        gameplay(prev_word, final_word, dictionary)

    if(dictionarycheck(input_word, dictionary) == False):
        print("Please enter a valid word" + '\n')
        print("Previous word was: " +  prev_word)
        gameplay(prev_word, final_word, dictionary)

    if(input_word == final_word):
        print("You did it! Congratulations")
    else:
        gameplay(input_word, final_word, dictionary)

###########################################
#game starts
startword = randomword(four_letter_words)
finalword = randomword(four_letter_words)

print("This is your starting word: " + startword)
print("This is your final word: " + finalword)

gameplay(startword, finalword, four_letter_words)

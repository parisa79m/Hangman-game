# -----------------
import random
lines = open("hangmanwords.txt").readlines()
line = lines[0]
words = line.split()
word_l = list()
for i in words:
    if 2 < len(i) <= 8:
        word_l.append(i)
word = random.choice(word_l)
"""
lines = open("hangmanwords.txt").readlines() : A list that contains only one item that contains all the words.
line = lines[0]: converts the previous list's item to a string.
words = line.split(), word_l = list(): Makes a list that contains all the words.
The for loop : make sure the length of words is what we want.
And finally choose a random word!

"""
# -------------------
correct_letters = list()
for i in word:
    correct_letters.append(i)
left_guesses = 8
x = len(word)
dashes_l = ["-"]*x
en_words = list(enumerate(correct_letters))
counter2 = 0
counter = 0
"""
The for loop: Separates the letters of the word.
en_words = list(enumerate(correct_letters)): Makes a list that each item is a tuple 
that contains the index of each letter in word.
"""
# -----------------------
print("This is a %s letter word" % x)
while left_guesses != 0:
        guess = input("guess a letter: ")
        left_guesses -= 1
        for tup in en_words:
            counter2 += 1
            if guess == tup[1]:
                dashes_l[tup[0]] = guess
                counter = 1
                left_guesses += 1

        if counter == 1:
            print("good guess!")
            print(" ".join(dashes_l))
            counter = 0
        elif counter == 0:
            print("oops wrong!")
            print(" ".join(dashes_l))
        if "-" not in dashes_l:
            print("you win!")
            break
        elif left_guesses == 0 and "-" in dashes_l:
            print("you lose! it was %s" % word)
"""
The while loop repeats 8 times and gets guesses.
Each time the while loop runs the for loop moves on every tuple in en_word list.
tup[0] ---> letter_index
tup[1] ---> letter 
So if the guess equals to tup[1] it will change the dash in dashes_l to the letter, based on that letter's index (tup[0])
And it goes on until you have no guesses left !
"""
# ----------------------



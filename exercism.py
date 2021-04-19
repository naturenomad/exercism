# https://exercism.io/tracks/python/exercises

# Exercises on the Python track
# 117 Python exercises in total

###########################################
# 1 - Hello World (easy)
###########################################

# The classical introductory exercise. Just say "Hello, World!"
# conditionals, optional values, text formatting

print("Hello, World!")


###########################################
# 2 - Two Fer (easy)
###########################################

# Create a sentence of the form "One for X, one for me."
# conditionals, optional values, text formatting

x=input()
print("One for {}, one for me".format(x))


###########################################
# 3 - Raindrops (easy)
###########################################

# Convert a number to a string, the content of which depends on the number's factors.

# conditionals, integers, text formatting

def raindrops():
    n=int(input("Please enter an integer number: "))
    factors=list()
    for i in range(1,n+1):
        if n%i == 0:
            factors.append(i)
    str="Factors in number {} are ".format(n)
    for f in factors:
        str += "{}, ".format(f)
    str = str[:-2]
    print(str)


###########################################
# 4 - High Scores (easy) - INCOMPLETE (UNCLEAR QUESTION)
###########################################

# Manage a player's High Score list

# sequences, text formatting, classes, conditionals


###########################################
# 5 - Matrix (easy)
###########################################

# Given a string representing a matrix of numbers, return the rows and columns of that matrix.

# integers, loops, matrices, type conversion

import numpy as np

# This interpretation of the question plays a little with numpy concepts
def matrix(str):
    
    #str = "1 2 3, 4 5 6, 7 8 9"
    
    # First, split the string into rows
    lst = str.split(", ")
    
    # Split the rows into columns
    lst = [i.split() for i in lst]
    
    # Convert strings to integers
    
    # Using numpy
    matr = np.array(lst)
    matr = matr.astype(np.int)
    
    # Or using map (ie the pythonic way)
    lst = [list(map(int, x)) for x in lst]
    
    # Print rows
    rowstr = "Rows: "
    for row in range(matr.shape[0]):
        rowstr += '{}, '.format(matr[row,:])
    print(rowstr[:-2])
    
    # Print columns
    colstr = "Columns: "
    for col in range(matr.shape[1]):
        colstr += '{}, '.format(matr[:,col])
    print(colstr[:-2])    
    

matrix("1 2 3, 4 5 6, 7 8 9")


###########################################
# 6 - Hamming (easy)
###########################################

# Calculate the Hamming difference between two DNA strands.

# algorithms, conditionals, filtering, logic, loops, sequences, sets, strings

# The Hamming distance between two strings of equal length is the number of positions at which the 
# corresponding symbols are different.

def hamming(str1, str2):
    hamming = 0
    
    # First check strings are same length
    if len(str1) != len(str2):
        return "Strands are not of equal length"
    
    for i in range(len(str1)):
        if str2[i] != str1[i]:
            hamming += 1
    
    return "Hamming distance is: {}".format(hamming)

hamming('GATTACA', 'GACTATA')


###########################################
# 7 - Isogram (easy)
###########################################

# Determine if a word or phrase is an isogram.

# algorithms, conditionals, loops, strings

# An isogram is a word with no letters repeated within the word. 

def isogram(phrase):
    phrase = phrase.replace(' ','')
    if len(set(phrase)) == len(phrase):
        return "Isogram"
    else:
        return "Not isogram"


isogram("This is a cow")
isogram("countryside")


###########################################
# 8 - Twelve Days (medium) - INCOMPLETE (NOT CHALLENGING)
###########################################

# Output the lyrics to 'The Twelve Days of Christmas'

# lists, strings, text formatting


###########################################
# 9 - Word Count (easy)
###########################################

# Given a phrase, count the occurrences of each word in that phrase.

# algorithms, logic, pattern recognition, strings, text formatting

import string

def wordcount(phrase):
    #Remove punctuation, make lowercase and split phrase into words
    phrase = phrase.translate(str.maketrans('', '', string.punctuation)).lower().split()
    
    #Make dictionary of list items and counts
    phrasedict = {word:phrase.count(word) for word in phrase}
    
    #Print the dict out nicely
    for word in phrasedict:
        print('{}: {}'.format(word, phrasedict[word]))

wordcount("This is not a pig, this is a mouse")



###########################################
# 10 - Scrabble Score (easy)
###########################################

# Given a word, compute the Scrabble score for that word.

# games, loops, maps, strings

# https://scrabble.hasbro.com/en-us/faq
#    (1 point)-A, E, I, O, U, L, N, S, T, R
#    (2 points)-D, G
#    (3 points)-B, C, M, P
#    (4 points)-F, H, V, W, Y
#    (5 points)-K
#    (8 points)- J, X
#    (10 points)-Q, Z

def scrabblescore(word):
    scoredict = {'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 
        'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10}
    score = 0
    for letter in word:
        score += scoredict[letter]
    print(score)

scrabblescore('blingblong')
scrabblescore('hi')


###########################################
# 11 - Acronym (easy)
###########################################

# Convert a long phrase to its acronym

# regular expressions, strings

import string

def acronym(phrase):
    #Remove punctuation, make lowercase and split phrase into word list
    phrase = phrase.translate(str.maketrans('', '', string.punctuation)).lower().split()
    
    #Get first letter, convert back to string, make upper case
    acronym = ''.join([i[0] for i in phrase]).upper()
    print(acronym)

acronym("why can't pigs fly")





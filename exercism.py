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


###########################################
# 12 - Kindergarten garden (easy) - INCOMPLETE (UNCLEAR TASK)
###########################################

# Given a diagram, determine which plants each child in the kindergarten class is responsible for.

# arrays. classes, optional values, variables


###########################################
# 13 - Grade School (easy)
###########################################

# Given students' names along with the grade that they are in, create a roster for the school

# conditionals, filtering, integers, lists, sorting, strings

def roster(children):
    # Accept a dictionary of children and their class    
    classes = set(children.values())
    for i in classes:
        print('#### Grade {} ####'.format(i))
        for child in children:
            if children[child] == i:
                print(child)
        print('\r')

children = {'ben':1, 'katey':2, 'biff':1, 'jane':3, 'peter':2, 'bingo':1, 'violet':3, 'bo':2}
roster(children)


###########################################
# 14 - Luhn (medium)
###########################################

# Given a number determine whether or not it is valid per the Luhn formula.

# algorithms, conditionals, loops, pattern matching, security

# The Luhn Algorithm is a simple checksum formula used to validate a variety of identification numbers, 
# such as credit card numbers.
# Also called the Modulus 10 Algorithm.

# (1) From the rightmost digit (excluding the check digit) and moving left, double the value of every second digit. 
# The check digit is neither doubled nor included in this calculation; the first digit doubled is the digit located 
# immediately left of the check digit. If the result of this doubling operation is greater than 9 (e.g., 8 × 2 = 16), 
# then add the digits of the result (e.g., 16: 1 + 6 = 7, 18: 1 + 8 = 9) or, equivalently, subtract 9 from the result 
# (e.g., 16: 16 − 9 = 7, 18: 18 − 9 = 9).
        
# (2) Take the sum of all the digits (including the check digit).

# (3) If the total modulo 10 is equal to 0 (if the total ends in zero) then the number is valid according to the Luhn 
# formula; otherwise it is not valid.

####

# Some data -

# All valid credit card numbers
valid1 = [4, 5, 3, 9, 6, 7, 7, 9, 0, 8, 0, 1, 6, 8, 0, 8]
valid2 = [5, 5, 3, 5, 7, 6, 6, 7, 6, 8, 7, 5, 1, 4, 3, 9]
valid3 = [3, 7, 1, 6, 1, 2, 0, 1, 9, 9, 8, 5, 2, 3, 6]
valid4 = [6, 0, 1, 1, 1, 4, 4, 3, 4, 0, 6, 8, 2, 9, 0, 5]
valid5 = [4, 5, 3, 9, 4, 0, 4, 9, 6, 7, 8, 6, 9, 6, 6, 6]

# All invalid credit card numbers
invalid1 = [4, 5, 3, 2, 7, 7, 8, 7, 7, 1, 0, 9, 1, 7, 9, 5]
invalid2 = [5, 7, 9, 5, 5, 9, 3, 3, 9, 2, 1, 3, 4, 6, 4, 3]
invalid3 = [3, 7, 5, 7, 9, 6, 0, 8, 4, 4, 5, 9, 9, 1, 4]
invalid4 = [6, 0, 1, 1, 1, 2, 7, 9, 6, 1, 7, 7, 7, 9, 3, 5]
invalid5 = [5, 3, 8, 2, 0, 1, 9, 7, 7, 2, 8, 8, 3, 8, 5, 4]

# Can be either valid or invalid
mystery1 = [3, 4, 4, 8, 0, 1, 9, 6, 8, 3, 0, 5, 4, 1, 4]
mystery2 = [5, 4, 6, 6, 1, 0, 0, 8, 6, 1, 6, 2, 0, 2, 3, 9]
mystery3 = [6, 0, 1, 1, 3, 7, 7, 0, 2, 0, 9, 6, 2, 6, 5, 6, 2, 0, 3]
mystery4 = [4, 9, 2, 9, 8, 7, 7, 1, 6, 9, 2, 1, 7, 0, 9, 3]
mystery5 = [4, 9, 1, 3, 5, 4, 0, 4, 6, 3, 0, 7, 2, 5, 2, 3]

####

# Optional function to turn a number into a numeric list for the luhn function
def makelist(num):
    return [int(x) for x in str(num)]

makelist(123456789)

####

def luhndoubling(num):
    num = 2*num
    if num > 9:
        num = num - 9
    return num

def luhn(lst):
    # First, luhndoubling every second digit from right excluding check digit :
    lst.reverse()
    lst = [luhndoubling(value) if key % 2 == 1 else value for key,value in enumerate(lst)]
    # Sum must be divisible by 10
    if sum(lst) % 10 == 0:
        return 'Valid Luhn Number'
    else:
        return 'Invalid Luhn Number'

luhn(valid1)
luhn(valid2)
luhn(valid3)
luhn(valid4)
luhn(valid5)
luhn(invalid1)
luhn(invalid2)
luhn(invalid3)
luhn(invalid4)
luhn(invalid5)
luhn(mystery1)
luhn(mystery2)
luhn(mystery3)
luhn(mystery4)
luhn(mystery5)




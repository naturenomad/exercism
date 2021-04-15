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




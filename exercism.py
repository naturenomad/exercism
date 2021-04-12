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
# 2 - Raindrops (easy)
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

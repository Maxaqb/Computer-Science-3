#===============================================================#

# Code 1

def greet_students (name, nChar):
    for i in range(nChar):
        print(name[i])

name = input("Enter a Name : ")
nChar = input("Enter any numeric number : ")
nChar = int(nChar)
greet_students(name, nChar)


# a) The Output: 
#
#       J
#       o
#       s
#       e
#       p
#       
#  This will be the output since the loop only iterated 
#  up to the range given (5)
#
#
#  b) The Output:
#       
#       J
#       o
#       s
#       e
#       p
#       h
#       
#       T
#       h
#       e
#       
#       D
#       r
#       e
#       a
#       m
#       e
#       r
#       IndexError: string index out of range
#
#  This will be the output because the range inputted
#  exceeds the amount of characters needed and when i
#  hits 18, name[18] doesn't exist
#
#  c) I could modify the code using try & except:

def greet_students (name, nChar):

    try:
        for i in range(nChar):
            print(name[i])

    except IndexError:
        print("nChar exceeds the amount of characters needed")

name = input("Enter a Name : ")
nChar = input("Enter any numeric number : ")
nChar = int(nChar)
greet_students(name, nChar)

#===============================================================#

# Code 2

def greet_students(name, nChar):
    for i in range(nChar)
        print(name[0 : nChar])

name = input("Enter a Name")
greet_students(name, len(name))


# a) Finding the syntax error and fix
#
#   There's a missing colon after the for loop's argument
#   and to fix it, just add a colon at the end of the line:
#   
#               for i in range(nChar):
#
#  b) Name as an Inverted Triangle

def greet_students (name, nChar):
    for i in range(nChar):
        print(name[0: nChar - 1])

name = input("Enter a Name")
greet_students(name, len(name))

#===============================================================#
#
# Code 3

n = 0
while n < 1 or n > 100:
    n = input("Enter a Number from 1 to 100 : ")
    n = int(n)

print("Sum of all squared number is", sum_of_squared(n))

# a) Function/s making 

def sum_of_squared(n):
    total = 0

    for i in range(1, n + 1):
        total += i**2

    return total

#===============================================================#
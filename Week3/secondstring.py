# This is Weekly Task 03
# The script will requets that a user enter a string
# Every second letter of this string will be output in reverse
# Author: Kieran Mullany
# Version 1

# Take in an input string and assign it to variable "inputString"
inputString = input("Please enter a string: ")

# The task requires that the second letter of this string be output so whitespace is stripped
#print(inputString.replace(" ","") [::-2])

# Amendment - example on page shows output with whitespace and punctuation marks
print(inputString [::-2])


# Script to count the number of e chars in a file
# Author Kieran Mullany

filename = "test.txt"
count = 0
with open(filename,"r") as f:
    for lines in f:
        for words in lines:
            for letter in words:
                if letter == 'e' or letter == 'E':
                    count += 1
print(count)
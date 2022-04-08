# Script to count the number of e chars in a file
# Author Kieran Mullany

#filename = "test.txt"               #hardcoded filename used for testing
import sys                           #module needed for command line args
from os.path import exists           #we need this to check existance of file - ref 1

if exists(sys.argv[1]):
    filename = sys.argv[1]               #[1] is the first arg which should be our file
else:
    print("ERROR: This is not a valid file")
count = 0
print(f"FILE = {filename}")
with open(filename,"r") as f:
    for lines in f:
        for words in lines:
            for letter in words:
                if letter == 'e' or letter == 'E':
                    count += 1
print(count)
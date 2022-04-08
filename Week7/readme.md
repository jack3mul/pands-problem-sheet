This is a python script which counts the numbers of the letter 'e' or 'E' in a file
The script is very straight forward and is working using a hard coded file name

The script will now be modified to accept a file inputted at a prompt

I learned a new way of checking a files existence which I like so I used it in this script
ref 1 -> https://www.pythontutorial.net/python-basics/python-check-if-file-exists/

The script takes a command line argument - method known from python experience and other programming knowledge, it checks if the file is supplied and then if it exists. If it doesnt meet this conditions the script will not continue.

If the script runs it drills down into the file, word by word in each line in a primitive way. This is a method I thought of. it doesnt use any inbuilt methods / regex or anything other pythonic way, it is simple and uses simple comparison to find the letter and increment the count.


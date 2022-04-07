# This program is my submission for weekly task 4
# The program requests an input - a positive number and then completes a series of calculations 
# until the number is equal to 1
# If the current value is even, the program divides it by 2
# If the current value is odd, the program multiplies it by 3 and adds 1
# The values are all printed in a line as output  
# Author Kieran Mullany

number = input("Enter a positive integer please: ")

current_number = int(number)
print(current_number, end=' ')                      #remove automatic \n from print

while current_number != 1:                          #condition keeps execution running
    if current_number % 2 == 0:                     #if even do this computation..
        current_number /= 2
        print(int(current_number), end=' ')         #print output - in a line - no decimals 
    else:                                           #if odd do this computation..
        current_number = (current_number * 3) + 1
        print(int(current_number), end=' ')
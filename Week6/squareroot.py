# Author Kieran Mullany
# Script to find a square root of an inputted number using Newton Method
# Newton Method is to use formula root = 0.5 * (X + (N / X))
# want to replace X on succesive steps

N = int(input("Enter a number to calculate its square root: "))
X = N                            #initial guess to start calculations
tolerance = 10 ** (-10)             #measure of accuracy - set high after testing low initially

while(abs(N - X*X) > tolerance):    #loop to feed back into the formula until a good estimate is found
    root = 0.5 * (X + (N / X))
    X = root                        #switch result into X variable for next run through loop

print(f"The square root of {N} is {X}")    #print result
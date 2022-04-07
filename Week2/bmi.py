# This program calculates a person's BMI
# The user is requested to input their height in centimetres and their weight in kilograms
# The program then calculated and returned their BMI
# Author: Kieran Mullany


weight = input("Enter weight (kg): ")
height = input("Enter height (cm): ")
# Adjust variable to metres
heightM = int(height) / 100

BMI = int(weight) / (heightM ** 2)

# confine print statement of BMI to two decimal places   
BMI_print = "{:.2f}".format(BMI)

print("The BMI is (kg/m2): {}".format(BMI_print))
# BMI Calculator
#Formula: weight (lb) / [height (in)]^2 
# Import is used to get the content from a pre developed libarary
import math

height = input("Enter your height in Inches\n")
weight = input("Enter your weight in Lbs\n")

height_in = float(height)
weight_in = int(weight)

# performing operations in python in in-line manner
bmi = weight_in / height_in ** 2

# print out the results
print(bmi)

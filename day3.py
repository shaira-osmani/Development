#Create a program using maths and f-strings that tell us 
#how many weeks we have left, if we live until 90 years old.

age = input("How old are you?\n")

#int() is a built-in function used to change the format of a data type.
# In here the input function gets all data in String format but for calculation we need in integer format hence we use the function.
years = 90 - int(age)
weeks = years * 52

print(f"You have {weeks} left.")
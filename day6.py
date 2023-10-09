# Leap Year

# Question
# Ask the usr for an input and then decide whether the typed year is a leap Year.
# What is a leap year?
# A normal year is 365 days, leap years have 366 days, with an extra day in February.
# The logic of solving this problem is:
# On every year that is divisible by 4 with no reminder
# Except every year that us evenly divisible by 100 with no reminder.
# Unless the year is also divisible by 400 with no reminder.

# Maths

# e.g year -> 2000

# 2000 / 4 = 500 (Leap)

# 2000 / 100 = 20 (Not leap)

# 2000 / 400 = 5 (leap)

# so the year 2000 is a leap year

# 2100 / 4 = 525 (Not leap)

# 2100 / 100 = 21 (Not Leap)

# 2100 / 400 = 5.25 (Not leap)


# Important Concept to learn
#  Mode or Modules 
# The statistics.mode() method calculates the mode (central tendency) of the given numeric or nominal data set.


# Which year do you want to check?

year = int(input())

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Leap year")

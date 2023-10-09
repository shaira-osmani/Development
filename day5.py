#BMI 2.0

height = float(input())

weight = int(input())

bmi = weight / height ** 2

if bmi < 18.5:
    print(f"Your BMI is {bmi}, You are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, You have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, You are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, You are Obese.")
else:
    print(f"Your BMI is {bmi}, You are clinicaly Obese.")

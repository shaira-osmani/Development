#if the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
# Round the result to 2 decimal numbers


print("Welcome to the tip calculator!\n")
bill = float(input("What was the total bill?\n"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?\n"))
people = int(input("How many people to split the bill with\n"))


tip_as_pct = tip / 100
total_tip_amt = bill * tip_as_pct
total_bill = bill + total_tip_amt
bill_per_person = total_bill / people
final_amt = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amt}")
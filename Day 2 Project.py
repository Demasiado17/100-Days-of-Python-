print("Tip Calculator")
people = float((input("How many people is the bill split by? \n")))
bill = float(input("How much was the bill?\n"))
tip= float(input("What % are you going to tip") ) / 100 + 1
final_pay = float(bill / people * tip)


print(f"You each will pay? {round(final_pay,2 )}")

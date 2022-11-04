income = float(input("Enter the annual income: "))
base = 85528
if income <= 0:
    tax = 0
elif income <= base:
    tax = (.18*income)-556.02
else:
    tax = 14839.02 + (.32*(income-base))

tax = round(tax, 0)
print("The tax is:", tax, "thalers")

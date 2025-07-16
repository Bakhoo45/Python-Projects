#Compound Interest Calculator

principal = 0
time = 0
rate = 0

while True:
    principal = float(input("Enter the principal amount: "))
    if principal < 0:
        print("Principal can't be less than 0. Please try again.")
    else:
        break

while True:
    time = int(input("Enter the time (in years): "))
    if time < 0:
        print("Time can't be less than 0. Please try again.")
    else:
        break

while True:
    rate = float(input("Enter the rate of interest: "))
    if rate < 0:
        print("Rate can't be less than 0. Please try again.")
    else:
        break

amount = principal * pow(1 + rate / 100, time)
compound_interest = amount - principal

print(f"Compound Interest: {compound_interest:.2f}")
print(f"Total Amount (Principal + Interest): {amount:.2f}")
# Name: Tkeyah Jefferies
# Date: 10/18/2025
# Assignment: P3LAB_JefferiesTkeyah
# Description: Make change using the fewest dollars/coins.

amount = float(input("Enter amount of money: "))

# Work in cents to avoid float rounding issues
cents = int(round(amount * 100))

dollars = cents // 100
cents %= 100

quarters = cents // 25
cents %= 25

dimes = cents // 10
cents %= 10

nickels = cents // 5
cents %= 5

pennies = cents

if dollars > 0:
    print(f"{dollars} dollar" if dollars == 1 else f"{dollars} dollars")
if quarters > 0:
    print(f"{quarters} quarter" if quarters == 1 else f"{quarters} quarters")
if dimes > 0:
    print(f"{dimes} dime" if dimes == 1 else f"{dimes} dimes")
if nickels > 0:
    print(f"{nickels} nickel" if nickels == 1 else f"{nickels} nickels")
if pennies > 0:
    print(f"{pennies} penny" if pennies == 1 else f"{pennies} pennies")

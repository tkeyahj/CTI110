#T'keyah Jefferies
#11/28/25
#Assignment Name: P5LAB
#Brief description of program: Self-checkout simulation that calculates change using random purchase amount

import random

def disperse_change(change):
    # Convert to cents first so we don't have decimal problems
    change_cents = int(round(change * 100))
    
    # Calculate dollars
    dollars = change_cents // 100
    change_cents = change_cents % 100
    
    # Calculate quarters
    quarters = change_cents // 25
    change_cents = change_cents % 25
    
    # Calculate dimes
    dimes = change_cents // 10
    change_cents = change_cents % 10
    
    # Calculate nickels
    nickels = change_cents // 5
    change_cents = change_cents % 5
    
    # Remaining cents are pennies
    pennies = change_cents
    
    # Show the change breakdown
    if dollars > 0:
        if dollars == 1:
            print(f"{dollars} Dollar")
        else:
            print(f"{dollars} Dollars")
    
    if quarters > 0:
        if quarters == 1:
            print(f"{quarters} Quarter")
        else:
            print(f"{quarters} Quarters")
    
    if dimes > 0:
        if dimes == 1:
            print(f"{dimes} Dime")
        else:
            print(f"{dimes} Dimes")
    
    if nickels > 0:
        if nickels == 1:
            print(f"{nickels} Nickel")
        else:
            print(f"{nickels} Nickels")
    
    if pennies > 0:
        if pennies == 1:
            print(f"{pennies} Penny")
        else:
            print(f"{pennies} Pennies")
    
    if dollars == 0 and quarters == 0 and dimes == 0 and nickels == 0 and pennies == 0:
        print("No change")


def main():
    print("Welcome to the Self-Checkout!")
    print("-" * 40)
    
    # Random amount that customer owes
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"\nAmount owed: ${amount_owed:.2f}")
    
    # Get cash from customer
    cash_paid = float(input("Enter the amount of cash you will put in: $"))
    
    # Figure out the change
    change = cash_paid - amount_owed
    
    print(f"\nChange: ${change:.2f}")
    
    # Show change breakdown
    if change > 0:
        disperse_change(change)
    elif change == 0:
        print("\nNo change owed.")
    else:
        print("\nInsufficient payment. Please add more money.")


# Call main function to run the program
main()

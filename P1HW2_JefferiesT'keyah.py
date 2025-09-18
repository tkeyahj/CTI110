# T'keyah Jefferies
# 09/18/2025
#P1HW2 - Travel Budget
# This program asks the user for a travel budget and expenses,
# calculates the total expenses, subtracts them from the budget,
# and displays the remaining balance.

# Pseudocode:
# 1. Ask user for budget
# 2. Ask user for destination
# 3. Ask user how much they will spend on gas
# 4. Ask user how much they will spend on accommodation
# 5. Ask user how much they will spend on food
# 6. Add expenses
# 7. Subtract from budget
# 8. Dsiplay travel destination, expenses, and remaining budget

budget = float(input("Enter your budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How mcuh will you spend on gas? "))
accommodation = float(input("How much will you spend on accommodation? "))
food = float(input("How much will you spend on food "))

total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

print("\n---------- Travel Summary ----------")
print(f"Destination: {destination}")
print(f"Initial Budget: ${budget:.2f}")
print(f"Gas: ${gas:.2f}")
print(f"Food: ${food:.2f}")
print("---------------------------------")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Balance: ${remaining_balance:.2f}")



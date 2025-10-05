# T'keyah Jefferies
# 10-4-2025
# P2HW1
# This program calculates and displays travel expenses with formatted output.

budget = float(input("Enter your budget:" ))
destination = input("Enter your travel destination:")
gas = float(input("How much do you think you will spend on gas? "))
hotel = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("How much do you need for food? "))

total_expenses = gas + hotel + food
remaining_balance = budget - total_expenses

print("\n------------Travel Expenses------------")
print(f"{'Location:':20} {destination}")
print(f"{'Initial Budget:':20} ${budget:,.2f}")
print(f"{'Fuel:':20} ${gas:,.2f}")
print(f"{'Accommodation:':20} ${hotel:,.2f}")
print(f"{'Food:':20} ${food:,.2f}")
print("----------------------------------------")
print(f"{'Reamaining Balance:':20} ${remaining_balance:,.2f}")


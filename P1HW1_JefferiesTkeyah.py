# Tkeyah Jefferies
# 09/15/2025
# P1HW1
# This program asks the user for numbers, calculates exponentiation and simple math, then displays the results. 
print("----Calculating Exponents----")
# Get base and exponent from user
base = int(input("Enter an integer as the base calue: "))
exponent = int(input("Enter an integer as the exponent: "))
# Calculate and display result
result = base ** exponent
print(f"\n{base} raised to the power of {exponent} is {result} !!")
print("\n----Addition and Subtraction----")
# Get three integers
num1 = int(input("\nEnter a starting integer: "))
num2 = int(input("Enter an integer to add: "))
num3 = int(input("Enter an integer to subtract: "))
# Perform calculations
final_result = num1 +num2 - num3
# Display result
print(f"\n{num1} + {num2} - {num3} is equal to {final_result}")
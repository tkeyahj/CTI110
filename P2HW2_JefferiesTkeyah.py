# Tkeyah [Your Last Name]
# October 2025
# P2HW2 - Grades List
# This program asks the user to enter grades for six modules,
# stores them in a list, and displays the lowest, highest, sum, and average.

# Pseudocode:
# 1. Ask user to enter grades for Module 1 through Module 6
# 2. Store grades in a list
# 3. Calculate lowest grade, highest grade, sum, and average
# 4. Display results formatted like the example

# Step 1: Get user input
mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))

# Step 2: Store grades in a list
grades = [mod1, mod2, mod3, mod4, mod5, mod6]

# Step 3: Perform calculations
low = min(grades)
high = max(grades)
total = sum(grades)
average = total / len(grades)

# Step 4: Display results
print('------------Results------------')
print(f'Lowest Grade:      {low:.1f}')
print(f'Highest Grade:     {high:.1f}')
print(f'Sum of Grades:     {total:.1f}')
print(f'Average:           {average:.2f}')
print('-------------------------------')

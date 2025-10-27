# T'Keyah Jefferies
# 10-26-2025
# P3HW1 - Debug and Complete Program
# This program collects six module grades, then displays the lowest,
# highest, total, and average, and reports the letter grade for the average.

# Enter grades for six modules
m1 = float(input('Enter grade for Module 1: '))
m2 = float(input('Enter grade for Module 2: '))
m3 = float(input('Enter grade for Module 3: '))
m4 = float(input('Enter grade for Module 4: '))
m5 = float(input('Enter grade for Module 5: '))
m6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list
grades = [m1, m2, m3, m4, m5, m6]

# determine lowest, highest, sum and average for grades
lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)

# display results
print('------------Results------------')
print(f'Lowest Grade:       {lowest:.1f}')
print(f'Highest Grade:      {highest:.1f}')
print(f'Sum of Grades:      {total:.1f}')
print(f'Average:            {average:.2f}')
print('----------------------------------------------')

# determine letter grade for average
if average >= 90:
    letter = 'A'
elif average >= 80:
    letter = 'B'
elif average >= 70:
    letter = 'C'
elif average >= 60:
    letter = 'D'
else:
    letter = 'F'

print(f'Your grade is: {letter}')







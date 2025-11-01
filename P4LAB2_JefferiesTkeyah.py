# T'Keyah Jefferies
# 10-27-2025
# P4LAB2_JefferiesTkeyah.py
# Program displays a multiplication table using loops

run_again = "yes"

while run_again.lower() == "yes":
    number = int(input("Enter an integer: "))

    if number >= 0:
        print(f"\nMultiplication table for {number}:")
        for i in range(1, 13):
            result = number * i
            print(f"{number} x {i} = {result}")
    else:
        print("Sorry, I cannot accept negative values.")

    run_again = input("\nWould you like to run the program again? (yes/no): ")

print("Thanks for using the program!")


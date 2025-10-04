#T'Keyah Jefferies
#10-03-25
#P2LAB2
#This program uses a dictionary to display a car's MPG and calculates gas needed for a trip.

cars_mpg = {
    'Camaro': 18.21,
    'Prius': 52.36,
    'Model S': 110,
    'Silverado': 26
}

keys = cars_mpg.keys()
print(keys)

car_choice = input("Enter a vehicle to see its mpg:")
mpg = cars_mpg[car_choice]
print(f"\nThe {car_choice} gets {mpg} mpg.\n")

miles = float(input(f"how many miles will you drive the {car_choice}? "))
gallons_needed = miles / mpg
print(f"\n{gallons_needed:.2f} gallons of gas are needed to drive the {car_choice} {miles:.1f} miles.")

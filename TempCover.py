# Create a program that converts temperatures between Celsius, Fahrenheit, and Kelvin.

print("1- Fahrenheit to Celsius")
print("2- Celsius to Fahrenheit")
print("3- Fahrenheit to Kelvin")
print("4- Kelvin to Fahrenheit")
print("5- Celsius to Kelvin")
print("6- Kelvin to Celsius")


userChoice = int(input("Choose an operation: "))

if userChoice == 1:
    degree = int(input("Degree in Fahrenheit: "))
    toCelsius = round((degree - 32) * 5 / 9, 2)
    print(f"{degree}F to C is {toCelsius}C")
elif userChoice == 2: 
    degree = int(input("Degree in Celsius: "))
    toFahren = round((degree * 9 / 5) + 32,2)
    print(f"{degree}C to F is {toFahren}F")

elif userChoice == 3:
    degree = int(input("Degree in Fahrenheit: "))
    toKelv = round(((degree - 32) / 1.8) + 273.15 , 2)
    print(f"{degree}F to K is {toKelv}K")
elif userChoice == 4:
    degree = int(input("Degree in Kelvin: "))
    toFahren = round(((degree - 273.15) * 1.8) + 32 , 2)
    print(f"{degree}K to F is {toFahren}F")
elif userChoice == 5:
    degree = int(input("Degree in Celsius: "))
    toKelv = round(degree + 273.15 , 2)
    print(f"{degree}C to K is {toKelv}K")
elif userChoice == 6:
    degree = int(input("Degree in Kelvin: "))
    toCelsius = round(degree - 273.15 , 2)
    print(f"{degree}K to C is {toCelsius}C")
else:
    print("Please choose from the above operations")
    
    

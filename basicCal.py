# Basic Calculator: Implement a calculator that performs addition, subtraction, multiplication, and division.

print("1- Addition")
print("2- Subtraction")
print("3- Multiplication")
print("4- division")

userC = int(input("Choose an operation: "))

if userC == 1:
    num1 = int(input("First Number: "))
    num2 = int(input("Second Number: "))
    result = num1 + num2
    print(f"The result is: {result}")

elif userC == 2:
    num1 = int(input("First Number: "))
    num2 = int(input("Second Number: "))
    result = num1 - num2
    print(f"The result is: {result}")
    
elif userC == 3:
    num1 = int(input("First Number: "))
    num2 = int(input("Second Number: "))
    result = num1 * num2
    print(f"The result is: {result}")

elif userC == 4:
    num1 = int(input("First Number: "))
    num2 = int(input("Second Number: "))
    if num2 == 0:
        print("Error: Can not divide by 0")
    else: 
        result = num1 / num2
        print(f"The result is: {result}")
else: 
    print("Please choose an operation from the above list.")

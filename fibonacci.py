# Fibonacci Sequence Generator: Write a program that generates the Fibonacci sequence up to a specified number of terms. 

print("Fibonacci Sequence Generator")
userI = int(input("Number of terms: "))
firstT = 0
secondT = 1
i = 0

if userI == 1:
    print(f"Fibonacci sequence upto {userI} is : {firstT}")
else:
    print("Fibonacci sequence:")
    while i < userI:
        print(firstT)
        toT = firstT + secondT
        firstT = secondT
        secondT = toT
        i += 1

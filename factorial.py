# Factorial Calculator: Create a program that computes the factorial of a given number.
print("Fibonacci Sequence Generator")
userI = int(input("Enter the number whose factorial is to be found: "))

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)
        
print(f"Factorial of {userI} is: {fact(userI)}")

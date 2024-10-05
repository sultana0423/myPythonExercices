# Fibonacci Sequence Generator: Write a program that generates the Fibonacci sequence up to a specified number of terms.
print("Fibonacci Sequence Generator")
userI = int(input("Enter the number whose factorial is to be found: "))

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)
        
print(f"Factorial of {userI} is: {fact(userI)}")

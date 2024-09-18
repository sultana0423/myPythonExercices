# Palindrome Checker: Write a program that checks if a given word or number is a palindrome.
print("Palindrome Checker.")
userInput = str(input("The Word: "))

def paliChecker(string):
    stringR = ''
    length = len(string)
    for i in range(length -1):
        stringR += string[i]
    print(stringR)

paliChecker(userInput)

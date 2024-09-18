# Palindrome Checker: Write a program that checks if a given word or number is a palindrome.
print("Palindrome Checker.")
userInput = str(input("The Word: "))

def paliChecker(string):
    stringR = ""
    length = len(string) - 1
    while length >= 0:
        stringR += string[length]
        length = length - 1
    print(stringR)
    print(f"Is the word palindrome? : {string == stringR}")

paliChecker(userInput)

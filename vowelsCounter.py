# Count Vowels in a String: Write a program that takes a string as input and counts the number of vowels (a, e, i, o, u) in it.

print("Vowels Counter")
userI = str(input("Enter word: "))
theVowels = []

for char in userI:
    c = char.lower()
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        theVowels.append(c)

print(f"Number of vowels: {len(theVowels)}")
        

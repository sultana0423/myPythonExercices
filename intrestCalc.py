#Simple Interest Calculator: Create a program that calculates simple interest based on the input of principal, rate of interest, and time.
print("Simple Interest Calculator")
p = int(input("Principal: "))
r = int(input("Rate of Interest: ")) / 100
t = int(input("Time: ")) 
def intrestCal(p,r,t):
  return p*r*t

print(intrestCal(p,r,t))

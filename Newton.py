# Implement the square root function using Newton's method. 
import math

#get imput from user
x = float(input("Enter a number: "))
y = float(input("Sqrt guess: "))

print("Math.sqrt(x): \t" + str(math.sqrt(x))) # Accurate sqrt

approx = y - ((y*y - x) / (2 * y))

for i in range (0,3):
    z = approx
    approx = y - ((y*y - x) / (2 * y))

print("Approximate: \t" + str(approx))
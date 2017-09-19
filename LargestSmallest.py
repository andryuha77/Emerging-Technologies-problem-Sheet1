numbers = []
print("Enter 5 numbers.")

for i in range (0,5):
    listItem = float(input(str(i + 1) + ": "))
    numbers.append(listItem)

print(numbers)

# https://stackoverflow.com/questions/2622994/python-finding-
lowest = min(float(i) for i in numbers)
print("Lowest: " + str(lowest))
highest = max(float(i) for i in numbers)
print("Highest: " + str(highest))

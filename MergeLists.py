list1 = []
list2 = []
listNew = []

print("Please enter 3 numbers for each list.")

print("List 1")
for i in range (0,3):
    listItem = float(input(str(i + 1) + ": "))
    list1.append(listItem)

print("List 2")
for i in range (0,3):
    listItem = float(input(str(i + 1) + ": "))
    list2.append(listItem)

listNew = list1 + list2

print()
print("List 1: " + str(list1))
print("List 2: " + str(list2))
print("New List: " + str(listNew))
# Adapted from https://docs.python.org/3/howto/sorting.html
print("Sorted List: " + str(sorted(listNew)))
print("Palindrome Test")

run = True

while run == True:
    word = input("Enter a word: ")
    print("Original: " + str(word))
    print("Reversed: " + str(word)[::-1])

    #https://stackoverflow.com/questions/931092/reverse-a-string-in-python
    if str(word) == str(word)[::-1]:
        print("This is word is a palindrome.")
        print()

    else:
        print("This is word is not a palindrome.")
        print()

    again = input("Test another word? Y/N: ")

    if again.lower() == "y":
        run = True
    elif again.lower() == "n":
        run = False
    else:
        again = input("Please enter Y/N: ")

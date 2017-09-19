from random import randint

print("Guess a number between 1 and 50.")
#generete random num
secretNum = randint(0,50)

# Take num from user
userGuess = int(input("Your guess: "))

count = []

while userGuess != secretNum:
    if userGuess < secretNum:
        print("Too low, try again.")
        userGuess = int(input())
        count.append(userGuess) # Add the guess to an array

    elif userGuess > secretNum:
        print("Too high, try again.")
        userGuess = int(input())
        alreadyGuessed.append(userGuess)

if userGuess == secretNum:
    print("Corect!")
    print("It took you " + str(len(set(count)) + 1) + " tries.")

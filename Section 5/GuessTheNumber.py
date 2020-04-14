#This is a guess the number game.
import random
print("What is your name?")
name = input()
secretNum = random.randint(1, 5)
print("I am thinking of a number 1 through 5")

#Ask the player to guess 6 times
for guessesTaken in range (1,5):
    print("Take a guess")
    guess = int(input())

    if guess < secretNum:
        print ("Too Low")
    elif guess > secretNum:
        print ("Too High")
    else:
        print("Correct")

print("You took " + str(guessesTaken) + " guesses. ")
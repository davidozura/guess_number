import random
import math

print("This is a secret number guessing game. You will hava a limited trials of guessing the number.")

name = input("But first, what is your name: ")

lowerNumber = 1
upperNumber = int(input("Please enter upper limit: "))

randonNumber = random.randint(lowerNumber, upperNumber)

chances_guess = round(math.log2(upperNumber - lowerNumber))

print(name, "in this game you will have ", chances_guess, "tries to guess the secret number between", lowerNumber, " and ", upperNumber, "number")

count = 0

while count < chances_guess:
    count = count + 1

    guess = int(input("Please guess the secret number:"))

    if randonNumber == guess:
        print("Congratulations, you have guessed the secret number in", count, "tries!!")
        break

    elif randonNumber < guess:
        print("The secret number is lower than you think.")

    elif randonNumber > guess:
        print("The secret number is higher than you think.")

if count >= randonNumber:
    print("More luck next time. The secret number was", randonNumber)

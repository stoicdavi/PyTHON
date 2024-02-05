#number guesing game
import random
print("Welcome to the number guessing game!")
number = random.randint(20, 25)
guess = int(input("Enter your guess: "))
if guess == number:
    print("Congratulations! You guessed the number!")
elif guess < number:
    print("Your guess is too low")
elif guess > number:
    print("Your guess is too high")
else:
    print("Sorry! The number was {}".format(number))
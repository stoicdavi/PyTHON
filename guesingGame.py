#Guesing game
guess = 0
guesses = 0
guesNo = 5
guessLimit = 3
while guesses != guessLimit:
    guess = int(input("Enter the guess number: "))
    guesses += 1
    if guess == guesNo:
        print(f"You have won with guess {guess} !")
        break
    else:
        print(f"Try again! You have {guessLimit - guesses} guesses left")
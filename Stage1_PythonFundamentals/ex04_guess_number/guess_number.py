import random

# Computer chooses a random number
secret_number = random.randint(1, 10)

# Loop until the user guesses correctly
while True:
    guess = int(input("Guess the number (1-10): "))

    if guess == secret_number:
        print("You guessed it! Congratulations!")
        break
    else:
        print("Wrong guess, try again.")

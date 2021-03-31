from random import seed
from random import randint
guess = input("Guess a number between 1-100")

# Seed Random Number Generator
seed(1)

# Generate the Random Number
for _ in range(1):
	randomNumber = randint(1, 100)
	print(randomNumber)

# Compare User Guesses with Generated Number
if guess > randomNumber:
    print("Hint: Guess a Lower Number")

elif guess < randomNumber:
    print("Hint: Guess a Higher Number")

elif guess == randomNumber:
    print("Correct!")
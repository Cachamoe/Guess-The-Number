randomNumber = 
guess = input("Guess a number between 1-100")

if guess > randomNumber:
    print("Hint: Guess a Lower Number")

if guess < randomNumber:
    print("Hint: Guess a Higher Number")

if guess = randomNumber:
    print("Correct!")
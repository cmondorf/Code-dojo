import random

while True:
    number = random.randint(0,10)
    guess = int(input("What do you think the secret number is?" ))
    if guess == number:
        again = input("Congratulations, you won!\nWould you like to play again?")
        if again == "yes":
            pass
        else:
            break
    elif guess > number:
        print("You guessed too high!")
    else:
        print("You guessed too low!")

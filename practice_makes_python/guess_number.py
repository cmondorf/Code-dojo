from random import randint

number = randint(0, 100)

while True:
    guess = int(input("Guess the number!"))
    if guess == number:
        break
    elif guess < number:
        print("Your guess was too low.")
    else:
        print("Your guess was too high.")

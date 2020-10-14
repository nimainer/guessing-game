from random import randint as ri

num = ri(1,100)

guess_limit1 = int(input("set the number of your guesses: "))

secret = num
guess_count = 0
guess_limit = guess_limit1
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count = guess_count + 1
    if guess == secret:
        print("you won !")
        break

    elif guess < secret:
        print('your guess is too small.')
    elif guess > secret:
        print("your guess is too large.")


print(f"you lost the number was {secret} !")
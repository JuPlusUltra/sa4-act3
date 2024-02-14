number = 10
print("I'm thinking of a number...")
guess = 0
guessnum = 0
while guessnum < 3:
    guess = (input("What number am I thinking of? "))

    if guess == 'q':
        break

    elif guess == number:
        print("Congratulations! You guessed the right number.")
        break

    else:
        print(f"Sorry! Try again.")
        chanceleft = 2 - guessnum
        print(f'You have {chanceleft} chance(s) left')
        guessnum = guessnum + 1

        
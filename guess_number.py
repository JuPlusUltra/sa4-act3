number = 10
print("I'm thinking of a number...")
guess = 0

while guess != number:
    guess = (input("What number am I thinking of? "))

    if guess == 'q':
        break

    elif guess == number:
        print("Congratulations! You guessed the right number.")
        break

    else:
        print(f"Sorry! Try again.")
        

    
    
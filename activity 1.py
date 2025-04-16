
#!/usr/bin/env python

import random

def main():
    """Start a colour guessing game."""
    print ("Guess the colour!")

    rainbow = [
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "violet"
        ]
    X = random.choice(rainbow)
    print(X)
    guess = None
    
    while X != guess:
        
        guess = str(input("What colour am I thinking of?"))

        if X == guess:
            print("You guessed {}.Congratulations you got it right!".format(guess))
            break
        else:
            print ("You guessed{}.Unfortunately its wrong.Try again!". format(guess))
main()   

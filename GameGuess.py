
from posixpath import split
from random import randint
from time import sleep


def gameguess():
    print('Hello. Whats your name ?', end=' ')
    name = input()
    secretNumber = randint(1, 20)
    print(f'Well, {name.title()} i am thinking a number between 0 and 20 try to guess!')


    for guesses in range(1, 7):
        print('Take a guess ... ', end=' ')
        guess = int(input())
        guessesLow = int(6 - guesses)
        if guess < secretNumber:
            if guessesLow == 0:
                print('You dont have chances anymore.')
            else:
                print('The number {}, is too low, please try again. You stil have '.format(
                    guess), str(guessesLow), 'Chances')
        elif guess > secretNumber:
            if guessesLow == 0:
                print('You dont have chances anymore.')
            else:
                print('The number {}, is too high, try again. You still have '.format(
                    guess), str(guessesLow), "Chances.")
        else:
            break  # These conditions are for correct question

    if guess == secretNumber:
        print('Congratulations {}, the number {} is correct. You guessed my number in'.format(
            name, guess), str(guesses), 'guesses!')
    else:
        print('The number i was thinking of was', str(secretNumber))


gameguess()

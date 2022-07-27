
from posixpath import split
from random import randint
from time import sleep


def gameguess():
    cont = 0
    print('Hello. Whats your name ?', end=' ')
    name = input()
    while True:
        secretNumber = randint(1, 20)
        if cont <= 0:
            print(
                f'Well, {name.title()} i am thinking a number between 0 and 20 try to guess!')
        else:
            print(
                f'lets go again, {name.title()} guess the number between 0 and 20!')
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
                break
        if guess == secretNumber:
            print('Congratulations {}, the number {} is correct. You guessed my number in'.format(
                name, guess), str(guesses), 'guesses!')
        else:
            print('The number i was thinking of was', str(secretNumber))
        continuar = input(str('DO u want to try again ? [Y/N] '))
        cont += 1
        if continuar not in 'Yy':
            break
    print(f"See you again soon {name}, good bye !! ")


gameguess()

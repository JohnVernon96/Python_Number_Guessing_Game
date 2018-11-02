# Name:     John Carvajal
# Class:    Organization of Programming Languages
# Teacher:  Dr. Cook
# Date:     10/14/2018
# Description: Guessing Game!

import random


#successOrFailFunction
def successOrFailFunction(guessIn,numberIn):
    if guessIn == numberIn:
        return 1;
    if guessIn != numberIn:
        return 0
    return


guessesTaken = 0
resetflag = 0
print('Hello! What is your name?')
Name = input()
number = random.randint(1, 100)
print('Hello, ' + Name + ', guess a number between 1 and 100. You start out with 6 tries!')

while resetflag == 0:

    while guessesTaken < 6:
        guess = input()
        guess = int(guess)
        guessesTaken = guessesTaken + 1
        isMatching = successOrFailFunction(guess,number)
        if isMatching == 0:
            if guess < number:
                guessesPrint = str(6 - guessesTaken)
                print('Your guess is too low. You have ' + guessesPrint + ' left')
            if guess > number:
                guessesPrint = str(6 - guessesTaken)
                print('Your guess is too high. You have ' + guessesPrint + ' left')
            if guess == number:
                break
        if isMatching == 1 or guessesTaken == 6:
            if guess == number:
                guessesTaken = str(guessesTaken)
                print('CORRECT!, ' + Name + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')
                break
            if guess != number:
                number = str(number)
                print(' ')
                print('FAILED! The number I was thinking of was ' + number + '.')
                print('You need more than 6 guesses?!')
                print('You suck at this game!')
                break
    print(' ')
    print('Do you want to play again ' + Name + '?')
    print(' ')
    print('Type a 1 if you want to play again or 0 if you wish to exit the program!')
    value = input()
    value = int(value)
    if value == 0:
        print('Program has finished')
        resetflag = 1
    if value == 1:
        print(' ')
        print('Time to play again ' + Name + '!')
        print('Guess another number between 1 and 100')
        number = random.randint(1, 100)
        guessesTaken = 0
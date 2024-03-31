NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('I am thinking of a', NUM_DIGITS, 'digit number. Try to guess what it is.')
    print('Here are some clues:')
    print('When I say:    That means:')
    print('  Pico         One digit is correct but in the wrong position.')
    print('  Fermi        One digit is correct and in the right position.')
    print('  Bagels       No digit is correct.')

    while True:
        secretNum = getSecretNum()
        print('I have thought up a number. You have', MAX_GUESSES, 'guesses to get it.')

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #', numGuesses)
                guess = input()

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                print('You got it!')
                break
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses. The answer was', secretNum)

        print('Do you want to play again? (yes or no)')
        if not input().lower().startswith('y'):
            break
    print('Thanks for playing!')
    
def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum
  
def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'
      
    clues = []
    
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)
      
if __name__ == '__main__':
    main()
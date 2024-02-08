import random
import os

os.chdir(r'E:\Python Programs')
file = open('hangmanwords.txt', 'r')                        # Opening the text file of words
word=str(random.choice(list(file))).strip()         # and choosing a random word from it

filled=[]
life=6
hangman=[['---------'],['|       |'],[],[],[],[],['-------']]        # Initialising the variables

for i in range(len(word)):                                  #Creating the Spaces for the
    filled+=['_']                                           # length word to be filled

print('Lets play Hangman!!\n'
      'You have 6 lives')
print(filled)

while life:
    guess=input("Guess a letter: ")                         # Getting user input for each letter using for loop

    if guess.lower() in word:                                # Checks whether the user
                                                            # given letter is present in the specified word
        for i in range(len(word)):                            # If yes, traverses through the word
            if guess==word[i]:
                filled[i]=word[i]                        # and replaces the space and fills it with the guessed letter

    else:                                                    # If no, reduces 1 from the life until life reaches 0
        life-=1                                              # Checks the life and updates the hangman drawing
        print(f'Your Guess {guess} is not present in the word. You lose a life')
        if life==5:
            hangman[2]='|   o'
        elif life==4:
            hangman[3]='|   |'
        elif life==3:
            hangman[3]='|  /|'
        elif life==2:
            hangman[3]='|  /|\\'
        elif life==1:
            hangman[4]='|  / '
        elif life==0:
            hangman[4]='|  / \\'
            print('Your life is over, You Lose')
            life=False                                                        # If life becomes 0, breaks out of for loop
    for i in hangman:                                                      # Prints both the word and hangman drawing
        print(*i)
    print(f'\n{filled}')

    if '_' not in filled:                                                # Checks if no remaining space is present
        print("Congrats, You have won)")              # Prints and breaks out of for loop
        break                                          # after all the letters are correctly guessed
print(word)
file.close()
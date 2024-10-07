#HANGMAN GAME

import random
print(r''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                     


              ''')
hangman= ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
lives=0
words_list=["walk","ball","bought","flyover","government","children"]
random_word=random.choice(words_list)
place_holder=" _ "*len(random_word)
print("===============WELCOME TO HANGMAN GAME================\n\n",place_holder)
right_letters=[]
game_over=False
while not game_over:
    display=""
    guess_word=input("\nGuess the Word :- ")
    for letter in random_word:
        if letter==guess_word.lower():
            display+=letter
            right_letters.append(letter)
        elif letter in right_letters:
            display+=letter
        else:
            display+=" _ "
    print("\n",display)
    if guess_word not in random_word:
        lives+=1
        print(f"\nYou guessed {guess_word},that's not in the word.you lose a life")
        print(f"\n=================You Have {6-lives} lives left=========== ")
        if lives==6:
            game_over=True
            print("\n=============YOU LOSS==========")
    else:
        print("\nYou already guessed")       
    
    if " " not in display:
        game_over=F=True
        print("\n========YOU WIN==========")
    print(hangman[lives])

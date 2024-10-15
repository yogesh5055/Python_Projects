#Guess the Number (1,100)

logo = """                                                                                                                                        

  _  _            _                ___                _              ___                
 | \| |_  _ _ __ | |__  ___ _ _   / __|_  _ ___ _____(_)_ _  __ _   / __|__ _ _ __  ___ 
 | .` | || | '  \| '_ \/ -_) '_| | (_ | || / -_|_-<_-< | ' \/ _` | | (_ / _` | '  \/ -_)
 |_|\_|\_,_|_|_|_|_.__/\___|_|    \___|\_,_\___/__/__/_|_||_\__, |  \___\__,_|_|_|_\___|
                                                            |___/                       
"""
print(logo)
import random
print("===================WELCOME TO NUMBER GUESSING GAME==============")
print("I'm thinking of a number between 1 to 100.")
guessed_number=random.randint(1,100)
level=input("Choose a difficulty.Type 'easy' or 'hard': ")
game_over=False
def user_choice(number):
    if number==guessed_number:
        global game_over
        game_over=True
        print("You Won.")
    elif number<guessed_number:
        print("Too low")
    elif number>guessed_number:
        print("Too High")

if level=="easy":
    print("You have 10 attempts remaining to guess the number.")
    number_of_attempts=10
    while number_of_attempts>=1 and not game_over:
                    if number_of_attempts==0:
                         print("========GAME OVER=======")
                         break
                    else:
                        number_of_attempts-=1
                        user_input=int(input("Make a guess: "))
                        user_choice(user_input)
                        if game_over:
                            break
                        if number_of_attempts!=0:
                            print("Guess again")
                            print(f"You have {number_of_attempts} remaining to guess the number.")
    
elif level=="hard":
    print("You have 5 attempts remaining to guess the number.")
    number_of_attempts=5
    while number_of_attempts>=1 and not game_over: 
                if number_of_attempts==0:
                    print("========GAME OVER=======")
                    break
                else:
                    number_of_attempts-=1
                    user_input=int(input("Make a guess: "))
                    user_choice(user_input)
                    if game_over:
                            break
                    if number_of_attempts!=0:
                        print("Guess again")
                        print(f"You have {number_of_attempts} remaining to guess the number.")
    

#ROCK PAPER SCISSORS GAME
import random
print("========ROCK======PAPER====SCISSORS========")
user_choice=input("Enter your Choice :-\n1.Rock\n2.Paper\n3.Scissor")
computer_options=['rock','paper','scissor'] 
computer_choice=random.choice(computer_options)

if user_choice.lower()=='rock':
    print("==========YOU===========")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    if computer_choice=='rock':
        print("====COMPUTER=====")
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")  
        print("===========GAME DRAW==================")
    
    elif computer_choice=='paper':
        print("====COMPUTER=====")    
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("==========YOU LOST=========")        
    elif computer_choice=='scissor':
        print("====COMPUTER=====")
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print("============YOU WIN============")  
elif user_choice.lower()=='paper':
    print("==========YOU===========")
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    if computer_choice=='rock':
        print("====COMPUTER=====")
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        print("============YOU WIN============") 
    elif computer_choice=='paper':
        print("====COMPUTER=====")
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("===========GAME DRAW==================")
    elif computer_choice=='scissor':
        print("====COMPUTER=====")
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print("==========YOU LOST=========") 
elif user_choice.lower()=='scissor':
    print("==========YOU===========")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    if computer_choice=='rock':
        print("====COMPUTER=====")
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        print("==========YOU LOST=========") 
    elif computer_choice=='paper':
        print("====COMPUTER=====")
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("============YOU WIN============") 
    elif computer_choice=='scissor':
        print("====COMPUTER=====")
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print("===========GAME DRAW==================")

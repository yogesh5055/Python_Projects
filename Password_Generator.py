#PASSWORD GENERATOR
import random
print("=====================WELCOME TO PASSWORD GENERATOR======================================")
number_of_letters=int(input("How many letters would you like in your password?"))
number_of_symbols=int(input("How many symbols would you like?"))
number_of_numbers=int(input("How many numbers would you like?"))
numbers=['1','2','3','4','5','6','7','8','9']
symbols=['#','$','+','!','@']
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
password=[]
for i in range(0,number_of_letters):
    letter_choice=random.choice(letters)
    password.append(letter_choice)
for i in range(0,number_of_symbols):
    symbol_choice=random.choice(symbols)
    password.append(symbol_choice)
for i in range(0,number_of_numbers):
    number_choice=random.choice(numbers)
    password.append(number_choice)
#-------- AVOID THE SEQUENCE PRINTING HERE I ADD SOME CODES -----
random.shuffle(password)
print("Your Password is:","".join(password))

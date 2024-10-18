#CALCULATOR PROGRAM 
print(r"""
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                              


""")

#addition
def add(a,b):
    return a+b

#subtraction

def sub(a,b):
    return a-b

#multiplication

def mul(a,b):
    return a*b

#divition

def div(a,b):
    return a/b

operations={"+":add,
            "-":sub,
            "*":mul,
            "/":div}

first_number=float(input("What's the first number? "))
loop=True
while loop:
  operation=input("""
   +
   -
   *
   /
   
   Pick an operation: """)
  second_number=float(input("What's the next number? "))
  answer=operations[operation](first_number,second_number)
  print(f"{first_number} {operation} {second_number} = {answer}")
  choice=input(f"Type 'y' to continue calculating with {answer}. or type 'n' to start a new calculation.")
  if choice=='y':
        first_number=answer
  if choice=='n':
       first_number=float(input("What's the first number? ")) 




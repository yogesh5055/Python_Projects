#Caesar Cipher
print(r'''


  ___ __ _  ___  ___  __ _ _ __ 
 / __/ _` |/ _ \/ __|/ _` | '__|
| (_| (_| |  __/\__ \ (_| | |   
 \___\__,_|\___||___/\__,_|_|        

      _       _               
     (_)     | |              
  ___ _ _ __ | |__   ___ _ __ 
 / __| | '_ \| '_ \ / _ \ '__|
| (__| | |_) | | | |  __/ |   
 \___|_| .__/|_| |_|\___|_|   
       | |                    
       |_|             

''')
print("=======WELCOME TO CAESAR CIPHER ENCODE/DECODE MESSAGE=========")

alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        
# here i use two function
'''def encode(text,shift):
    encode_text=""
    for i in text:
        index_position=alphabets.index(i)
        encode_text+=alphabets[(index_position+shift)%25]
    print(f"Your Encrypted Message is :- {encode_text}")

def decode(text,shift):
    decode_text=""
    for i in text:
        index_position=alphabets.index(i)
        decode_text+=alphabets[(index_position-shift)%25]
    print(f"Your Decrypted Message is :- {decode_text}")
    
'''
#In one function
def caesar_cipher(user_choice,text,shift):
        orginal_text=""
        if user_choice=="decode":
            shift *= -1
        for i in text:
            if i not in alphabets:
                orginal_text+=i 
            else:
                index_position=alphabets.index(i)
                new_position=(index_position+shift)%25
                orginal_text+=alphabets[new_position]
        print(f"Your {user_choice}d Message is :- {orginal_text}")

loop=True
while loop:
    user_choice=input("Type 'encode' to encrypt, Type 'decode' to decrypt :\n").lower()
    text=input("Enter your message:\n").lower()
    shift=int(input("Type the shift number:\n"))
    caesar_cipher(user_choice,text,shift)
    repeat=input("Type 'yes' if you want to go again.otherwise type 'no'.")
    if repeat=='no':
        print("=================THANK YOU=======================")
        loop=False
    



import pandas as pd
data=pd.read_csv("nato_phonetic_alphabet.csv")
new_dict={key.letter:key.code for (index,key) in data.iterrows() }
def generate_word():
  user_input =input("Enter a word :").upper()
  try:
     ans=[new_dict[letter]  for letter in user_input ]
  except KeyError:
    print("Sorry, only letters in the alphabet please.")
    generate_word()
  else:
    print(ans)
generate_word()



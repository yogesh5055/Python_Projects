import pandas as pd
data=pd.read_csv("nato_phonetic_alphabet.csv")
new_dict={key.letter:key.code for (index,key) in data.iterrows() }
user_input =input("Enter a word :").upper()
ans=[new_dict[letter]  for letter in user_input ]
print(ans)




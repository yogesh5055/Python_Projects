REPLACE="[name]"
with open("./Input/Names/invited_names.txt","r") as names:
    name=names.readlines()
    

with open("./Input/Letters/starting_letter.txt","r") as letter:
    content=letter.read()
    for i in name:
            x=content.replace(REPLACE,i.strip())
            with open(f"./Output/ReadyToSend/letter_for_{i.strip()}.txt","w") as letters:
                 letters.write(x)

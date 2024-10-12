#THE SECRET AUCTION PROGRAM
print(r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
''')
print("=============WELCOME TO SECRET ACTION ==================")
secret_action={}
loop=True
while loop:
    name=input("What's your name? :")
    bid=int(input("What's your bid? :$"))
    choice=input("Are there any other bidders? Type 'yes' or 'no'")
    secret_action[name]=bid
    print("\n"*100)
    if choice=='no':
        loop=False
for key in secret_action:
    maximum_bid=0
    if maximum_bid<secret_action[key]:
        maximum_bid=secret_action[key]
        
print(f"The winner is {key} with a bid of ${maximum_bid}.")

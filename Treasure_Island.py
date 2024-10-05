#Treasure Island Program
print(r"""                    _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
               '-._'-.|| |' `_.-'
                    '-.||_/.-' 
                                     """)
print("=======WELCOME TO TREASURE ISLAND GAME=======\nYou're in the Mission to Find the Treasure.")
user_direction=input("You're at a cross road.\nWhere do you want to go?\n1.Right\n2.Left\n'..........Type the choice..........'")
if user_direction.lower()=='left':
    island_choice=input("You've come to lake.\nNow you've two choices\n1.Swim\n2.Wait 'for boad'")
    if island_choice.lower()=='wait':
            door_choice=input("Now You're at Island.\nInfront of you there are three clour of doors.\nwhich door do you choose?\n1.Red\n2.Green\n3.Yellow")
            if door_choice.lower()=='yellow':  
                  print("*****************YOU WON*************")
            elif door_choice.lower()=='red':
                  print("*************YOU LOST*************")
            elif door_choice.lower()=='green':
                  print("*************YOU LOST*************")
    else:
        print("*************YOU LOST*************")
else:
    print("You fall into a hole\n*************YOU LOST*************")

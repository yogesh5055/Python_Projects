'''
This project is fully website based if want to check out this 
follow this link ----> https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json 
'''
while not at_goal():
    if wall_in_front():
        turn_left()
    if front_is_clear():
        move()
    if right_is_clear():
        turn_left()
        turn_left()
        turn_left()

# Characters
define e = Character("Emi")
define y = Character("Yolei")
define a = Character('Ara')

# Backgrounds
image dark_bg = ("#16171b")

# Animation
transform slide_out_right:
    xpos 0.95 
    ypos 0.95
    anchor (1.0, 1.0)
    zoom 0.8
    linear 1.0 xpos 1.5 

transform slide_in_right:
    xpos 1.5 
    ypos 0.95
    anchor (1.0, 1.0)
    zoom 0.8
    linear 1.0 xpos 0.95 


# Stats variables
$ strength = 1
$ dexterity = 2 
$ constitution = 1 
$ intelligence = 4
$ wisdom = 0 
$ charisma = -1 
$ proficency = 3 
$ expertise = 6

# Emi's stats page
default strength = 1
default dexterity = 2 
default constitution = 1 
default intelligence = 4
default wisdom = 0 
default charisma = -1 
default proficency = 3
default expertise = 6 


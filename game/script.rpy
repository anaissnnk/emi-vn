# Characters
define e = Character("Emi")

#Backgrounds
image emi_room = "bg/emis_room.png"

# The game starts here.
label start:
    show border onlayer screens 
    play music "reflexion.mp3" fadein 0.5
    scene emi_room with dissolve
    show emi_neutral at left with dissolve

    e "I'm standing on the left."
    e "The following is a lorem ipsum test in the small box."
    # This ends the game.

    return

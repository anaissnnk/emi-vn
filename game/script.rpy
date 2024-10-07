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
    e "The following is a dice roll test."

    #dice roll function
    $ d20roll = renpy.random.randint(1, 20)
    e "You rolled a [d20roll]"

    #second roll
    e "Let's try again"
    $ d20roll = renpy.random.randint(1, 20)
    e "This time, you rolled a [d20roll]"




    # This ends the game.
    return

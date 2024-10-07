# Characters
define e = Character("Emi")

#Backgrounds
image emi_room = "bg/emis_room.png"

# The game starts here.
label start:
    show border onlayer screens 
    play music "reflexion.mp3" fadein 0.5
    scene emi_room with dissolve
    show emi_neutral at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)

    e "I'm standing on the left."
    hide emi_neutral

    menu:
        e "The following is a dice roll test."
        "Roll the dice":
            #dice roll function
            $ d20roll = renpy.random.randint(1, 20)
            #hide textbox
            window hide
            pause 0.8
            show dice at Transform(zoom = 0.5):
                xpos 0.0 ypos 0.0
                ease 2.0 xpos 0.5 ypos 0.5
            pause 3.5
            hide dice
            e "You rolled a [d20roll]"
            e "Is it good?"
    
        "Don't roll the dice":
            e "You didn't roll the dice"


    #second roll
    # e "Let's try again"
    # $ d20roll = renpy.random.randint(1, 20)
    # e "This time, you rolled a [d20roll]"




    # This ends the game.
    return

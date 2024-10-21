label start:
    show border onlayer screens
    #TODO: add pensive music

    "My mom always made a fuss about my sleeping habits."
    "{i}\"There's nothing quite like enjoying a nice cup of tea and watching the sun rise.\"{/i}"
    "{i}\"I hope one day, you'll be able to enjoy the nice little things life has to offer.\"{/i}"
    "{i}\"Unlike the complete blockhead of a man I ended up marrying and who calls himself your father--\"{/i}"

    scene emi_room
    #TODO: add chill music
    show screen statButton
    show emi_neutral at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8) with dissolve

    e "Indeed, I believe there would be nothing better than to enjoy a quiet peaceful morning..."

    hide emi_neutral
    #TODO: stop chill music
    e "... without having to face the consequences of waking up late when I was on morning shift."

    #TODO: add dramatic music
    hide screen statButton
    scene dark_bg
    window hide
    pause 0.8
    # img slide animation
    show emi_chibi_sad at Transform(zoom = 0.6) with dissolve:
        truecenter
    pause 3.0
    hide emi_chibi_sad

    "test"







label template:
    show border onlayer screens 
    play music "reflexion.mp3" fadein 0.5

    scene emi_room
    show screen statButton

    show emi_neutral at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8) with dissolve

    e "I'm standing on the left."
    hide emi_neutral

    e "The following is an ending pic slide test"

    hide screen statButton
    scene dark_bg
    window hide
    pause 0.8
    # img slide animation
    show emi_chibi_sad at Transform(zoom = 0.6) with dissolve:
        truecenter
    pause 3.0
    hide emi_chibi_sad

    # back to main interface

    scene emi_room
    show screen statButton

    #check
    menu:
        e "The following is a charisma check."
        "Roll the dice":
            #dice roll function
            $ dice_roll, total = charisma_check(charisma)
            #hide textbox
            window hide
            pause 0.8
            #dice animation
            show dice at Transform(zoom = 0.5) with dissolve:
                xpos 0.0 ypos 0.0
                ease 2.0 xpos 0.5 ypos 0.5
            pause 3.5
            hide dice
            #declare result
            e "You rolled a [dice_roll]. Your charisma bonus is ([charisma]). The total is [total]."
            e "Let's try a roll with proficency."
            $ dice_roll, total = intelligence_proficency_check(intelligence, proficency)
            #hide textbox
            window hide
            pause 0.8
            #dice animation
            show dice at Transform(zoom = 0.5) with dissolve:
                xpos 0.0 ypos 0.0
                ease 2.0 xpos 0.5 ypos 0.5
            pause 3.5
            hide dice
            #declare result
            e "You rolled a [dice_roll]. Your intelligence bonus is ([intelligence]) and your proficency is ([proficency]). The total is [total]."
            e "Did that work?"
            
            
            e "Now let's try expertise."
            $ dice_roll, total = intelligence_expertise_check(intelligence, expertise)
            #hide textbox
            window hide
            pause 0.8
            #dice animation
            show dice at Transform(zoom = 0.5) with dissolve:
                xpos 0.0 ypos 0.0
                ease 2.0 xpos 0.5 ypos 0.5
            pause 3.5
            hide dice
            #declare result
            e "You rolled a [dice_roll]. Your intelligence bonus is ([intelligence]) and your expertise is ([expertise]). The total is [total]."
            e "Did that work?"

    
        "Don't roll the dice":
            e "You didn't roll the dice"

    # This ends the game.
    return

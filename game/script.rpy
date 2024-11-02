label start:
    show border onlayer screens
    #TODO: add pensive music
    play music "reflexion.mp3" fadein 0.5

    "My mom always made a fuss about my sleeping habits."
    "{i}\"There's nothing quite like enjoying a nice cup of tea and watching the sun rise.\"{/i}"
    "{i}\"I hope one day, you'll be able to enjoy the nice little things life has to offer.\"{/i}"
    "{i}\"Unlike the complete blockhead of a man I ended up marrying and who calls himself your father--\"{/i}"

    scene workshop
    #TODO: add chill music
    show screen statButton
    show emi_neutral at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8) with dissolve
    voice "voice/emi_laugh.mp3"
    e "Indeed, I believe there would be nothing better than to enjoy a quiet peaceful morning..."

    hide emi_neutral
    #TODO: stop chill music
    e "... without having to face the consequences of waking up late when the shop was exceptionally open this morning."

    #TODO: add dramatic music
    #TODO: add scene with chibi?

    scene workshop
    show screen statButton
    #TODO: add silly music
    show emi_sad2 at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)
    e "I know it was my fault for opening the shop late, but still..."
    e "Those adventurers didn't have to be so mean."

    hide emi_sad2
    show emi_annoyed at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)
    e "And it wasn't such a big deal that they had to kick Wabee."
    e "{i}Nobody hurts Wabee.{/i}"
    e "..."
    hide emi_annoyed
    show emi_angry at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)
    e "{i}I hope they get attacked by a bugbear.{/i}"
    e "{i}Assholes.{/i}"


label path:
    #TODO: check for new music?
    scene workshop
    hide emi_annoyed
    show emi_sigh at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)
    e "{i}Sigh{/i}. At least they're gone, and I can finally close the shop!"
    hide emi_sigh 
    show emi_smirk at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)
    e "I'll have Master Baltazar treat me at the tavern once he's back. That's the least he can do!"
    hide emi_smirk
    show emi_neutral at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)
    e "Now, what should I do for the rest of the day?"
    hide emi_neutral

    # menu:
    #     "Choose Emi's path."

    #     #CRAFT PATH
    #     "Craft the day away.":
    #         jump craft_path

    #     #ARA's PATH
    #     "Take a stroll in the forest.":
    #         jump ara_path

    #     #YOLEI'S PATH
    #     "Is that beer on the kitchen counter??":
    #         jump yolei_path













label template:
    show border onlayer screens 
    play music "reflexion.mp3" fadein 0.5

    scene workshop
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

    scene workshop
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

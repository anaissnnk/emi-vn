label yolei_path:
    scene kitchen with dissolve
    show screen statButton
    pause 0.3

    show emi_neutral at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8) with dissolve
    e "Let's see, I think it was around here..."
    e "Herbal influsion, sunflower seeds, some milk, an antidone, ..."
    voice "voice/emi_ok_neutral.wav"
    hide emi_neutral
    show emi_happy at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)
    e "There it is!"
    hide emi_happy
    show emi_surprised at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)
    voice "voice/emi_what_confused.mp3"
    e "Wait, that's not beer."
    hide emi_surprised

    menu:
        e "What is this?"
        "Examine the bottle (Investigation).":
            jump examine_bottle
        "Leave it be.":
            jump unknown_bottle


label examine_bottle:
    $ dice_roll, totalBottleCheck = intelligence_expertise_check(intelligence, expertise)
    window hide
    pause 0.8
    show dice at Transform(zoom = 0.5) with dissolve:
        xpos 0.0 ypos 0.0
        ease 2.0 xpos 0.5 ypos 0.5
    pause 3.5
    hide dice

    "You rolled a [dice_roll]. Your intelligence bonus is ([intelligence]) and your expertise is ([expertise]). The total is [totalBottleCheck]."
    if totalBottleCheck > 5 and dice_roll != 1: 
        $ bottleKnowledge = True
        show emi_neutral at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8) with dissolve
        e "There's a note behind the bottle."
        hide emi_neutral
        show emi_surprised at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)
        voice "voice/emi_what_confused.mp3"
        e "Let's see... It's... a balding potion?"
        voice "voice/emi_why_brat.mp3"
        e "Why would Miss Elizabeth..."
        e "..."
        e "I guess all relationships are complicated."
        hide emi_surprised
        jump after_bottle


label unknown_bottle:
    show emi_surprised at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8) with dissolve
    e "I don't know what this is. It's better not to touch it."
    hide emi_surprised
    jump after_bottle

label after_bottle:
    "After the bottle scene."

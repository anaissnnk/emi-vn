label yolei_path:
    scene kitchen with dissolve
    show screen statButton
    pause 0.3

    show emi_neutral at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8) with dissolve
    e "Let's see, I think it was around here..."
    e "Herbal influsion, sunflower seeds, some milk, an antidone, ..."
    voice "voice/emi_ok_neutral.wav"
    e "There it is!"
    hide emi_neutral
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
    $ dice_roll, total = intelligence_expertise_check(intelligence, expertise)
    window hide
    pause 0.8
    show dice at Transform(zoom = 0.5) with dissolve:
        xpos 0.0 ypos 0.0
        ease 2.0 xpos 0.5 ypos 0.5
    pause 3.5
    hide dice

    "You rolled a [dice_roll]. Your intelligence bonus is ([intelligence]) and your proficency is ([proficency]). The total is [total]."
    e "Did that work?"
    jump after_bottle



label unknown_bottle:
    e "Heh, better no touch it."
    jump after_bottle



label after_bottle:
    "After the bottle scene."

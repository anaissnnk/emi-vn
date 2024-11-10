label yolei_path:
    scene kitchen with dissolve
    show screen statButton
    pause 0.3

    show emi_neutral at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8) with dissolve
    e "Let's see, I think it was around here..."
    e "Herbal influsion, sunflower seeds, rose perfurme, some milk, a vial of antidote, ..."
    voice "voice/emi/emi_ok_calm.mp3"
    hide emi_neutral
    show emi_happy at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)
    voice "voice/emi/emi_laugh2.mp3"
    e "There it is!"
    hide emi_happy
    show emi_surprised at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)
    voice "voice/emi/emi_what_confused.mp3"
    e "Wait, that's not beer."
    hide emi_surprised
    hide screen statButton

    menu:
        e "What is this?"
        "Examine the bottle (Investigation).":
            jump examine_bottle
        "Leave it be.":
            jump unknown_bottle


label examine_bottle:
    hide screen statButton
    $ dice_roll, totalBottleCheck = intelligence_expertise_check(intelligence, expertise)
    window hide
    pause 0.8
    show dice at Transform(zoom = 0.5) with dissolve:
        xpos 0.0 ypos 0.0
        ease 2.0 xpos 0.5 ypos 0.5
    pause 3.5
    hide dice

    "You rolled a [dice_roll]. Your intelligence bonus is ([intelligence]) and your expertise is ([expertise]). The total is [totalBottleCheck]."
    if dice_roll != 1 and totalBottleCheck > 5: 
        $ bottleKnowledge = True

        show screen statButton
        show emi_neutral at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8) with dissolve
        e "There's a note behind the bottle."
        hide emi_neutral
        show emi_surprised at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)
        e "Let's see... It's a balding potion?"
        voice "voice/emi/emi_why_neutral.mp3"
        e "Why would Miss Elizabeth..."
        e "..."
        e "I guess all relationships are complicated."
        hide emi_surprised
        jump after_bottle

    elif dice_roll == 1:
        jump unknown_bottle


label unknown_bottle:
    show screen statButton
    show emi_surprised at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8) with dissolve
    e "I don't know what this is. It's better not to touch it."
    $ bottleKnowledge = False
    hide emi_surprised
    jump after_bottle


label after_bottle:
    show emi_neutral at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)
    e "Well, there's no beer but I could use a nice cup of tea!"
    e "Where's my cup--"
    play sound "sound/doorbell.mp3"
    hide emi_neutral 
    show emi_surprised at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)
    e "?"
    e "Why is the bell ringing? I'm sure I closed the door..."
    play sound "sound/doorbell.mp3"
    e "..."
    e "Could it be..."
    hide emi_surprised 
    show emi_neutral at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)
    e "Yolei?"
    stop music fadeout 0.5


label yolei:
    play music "music/upbeat.mp3" fadein 0.5
    scene workshop with dissolve 
    show screen statButton
    pause 0.3
    show emi_neutral at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8) with dissolve
    show yolei_neutral at slide_in_right with dissolve
    pause 0.4
    e "{i}Yup, that's him.{/i}"
    voice "voice/emi/emi_hello.mp3"
    e "Hello hello."
    hide yolei_neutral
    show yolei_smile at Transform(xpos = 0.95, ypos = 0.95, anchor = (1.0, 1.0), zoom = 0.8)
    voice "voice/yolei/yolei_hum.mp3"
    y "Hey!"
    e "Hiding from the circus again?"
    hide yolei_smile
    show yolei_grin at Transform(xpos = 0.95, ypos = 0.95, anchor = (1.0, 1.0), zoom = 0.8)
    voice "voice/yolei/yolei_laugh.mp3"
    y "I'm not hiding from them. I'm {i}avoiding{/i} them."
    hide emi_neutral
    show emi_surprised at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)
    e "Sure, whatever you say..."
    hide yolei_grin 
    show yolei_neutral at Transform(xpos = 0.95, ypos = 0.95, anchor = (1.0, 1.0), zoom = 0.8)
    y "Whatcha doing today? Where's the roommate?"
    hide emi_surprised 
    show emi_neutral at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)
    voice "voice/emi/emi_actually_neutral.mp3"
    e "I don't know. She had already left when I woke up."
    e "{i}Ara's new hobby is food hunting, so maybe she went to the forest?{/i}"
    e "And I was just having tea."
    hide yolei_neutral 
    show yolei_bored at Transform(xpos = 0.95, ypos = 0.95, anchor = (1.0, 1.0), zoom = 0.8)
    voice "voice/yolei/yolei_confused.mp3"
    y "You're drinking bitter warm water again?"
    hide emi_neutral 
    show emi_sigh at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)
    voice "voice/emi/emi_how.mp3"
    e "It's {i}tea{/i}."
    y "Sure. Whatever {i}you{/i} say."
    voice "voice/yolei/yolei_confused.mp3"
    y "Do you have something else to drink? Something more {i}interesting{/i}?"
    hide yolei_bored 
    hide emi_sigh 
    hide screen statButton

    menu:
        e "Do I have a different drink for Yolei?"

        "Bitter warm water only.":
            jump no_yolei_ending 

        "Nope.":
            jump no_yolei_ending 
            
        "Make him drink the potion I found" if bottleKnowledge:
            jump yolei_bald_path


label no_yolei_ending:
    show screen statButton
    show emi_neutral at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)
    show yolei_bored at Transform(xpos = 0.95, ypos = 0.95, anchor = (1.0, 1.0), zoom = 0.8)
    e "Sadly, I only have bitter warm water that smells like flower."
    voice "voice/yolei/yolei_disappointed.mp3"
    y "Boring. I'm gonna get a {i}real{/i} drink outside."
    hide emi_neutral
    show emi_surprised at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)
    e "Milk?"
    hide yolei_bored
    show yolei_grin at Transform(xpos = 0.95, ypos = 0.95, anchor = (1.0, 1.0), zoom = 0.8)
    voice "voice/yolei/yolei_victorious.mp3"
    y "Your words, not mine."
    e "That's not--"
    hide yolei_grin
    show yolei_grin at slide_out_right
    pause 0.4
    hide emi_surprised
    show emi_sigh at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)
    e "And he's gone."
    hide emi_sigh 
    show emi_neutral at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)
    e "Guess I'll just spend some nice alone time today."
    stop music fadeout 0.5
    jump craft_path



label yolei_bald_path:
    show screen statButton
    "Bald Yolei ending"




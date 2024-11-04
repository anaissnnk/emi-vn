label yolei_path:
    scene kitchen with dissolve
    show screen statButton
    pause 0.3

    show emi_neutral at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8) with dissolve
    e "Let's see, I think it was around here..."
    e "Herbal influsion, sunflower seeds, experimental poison, experimental toxine, a vial of antidote, ..."
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
    if dice_roll != 1 and totalBottleCheck > 5: 
        $ bottleKnowledge = True

        show emi_neutral at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8) with dissolve
        e "There's a note behind the bottle."
        hide emi_neutral
        show emi_surprised at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)
        voice "voice/emi_what_confused.mp3"
        e "Let's see... It's... a balding potion?"
        e "Why would Miss Elizabeth..."
        e "..."
        e "I guess all relationships are complicated."
        hide emi_surprised
        jump after_bottle

    elif dice_roll = 1:
        jump unknown_bottle


label unknown_bottle:
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


label yolei:
    play music "music/upbeat.mp3" fadein 0.5
    scene workshop with dissolve 
    show screen statButton
    pause 0.3
    show emi_neutral at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8) with dissolve
    show yolei_neutral at Transform(xpos = 0.95, ypos = 0.95, anchor = (1.0, 1.0), zoom = 0.8) with dissolve
    e "{i}Yup, that's him.{/i}"
    voice "voice/emi_hello.mp3"
    e "Hello hello."
    hide yolei_neutral
    show yolei_smile at Transform(xpos = 0.95, ypos = 0.95, anchor = (1.0, 1.0), zoom = 0.8)
    y "Heya!"
    e "Hiding from the circus again?"
    hide yolei_smile
    show yolei_grin at Transform(xpos = 0.95, ypos = 0.95, anchor = (1.0, 1.0), zoom = 0.8)
    y "I'm not hiding from them. I'm {i}avoiding{/i} them."
    hide emi_neutral
    show emi_surprised at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)
    e "Sure, whatever you say..."
    hide yolei_grin 
    show yolei_neutral at Transform(xpos = 0.95, ypos = 0.95, anchor = (1.0, 1.0), zoom = 0.8)
    y "Whatcha doing today? Where's the roommate?"
    hide emi_surprised 
    show emi_neutral at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)
    e "Beats me. Ara probably went to the forest."
    e "{i}Her new hobby is hunting for food so...{/i}"
    e "And I was just having tea."
    hide yolei_neutral 
    show yolei_bored at Transform(xpos = 0.95, ypos = 0.95, anchor = (1.0, 1.0), zoom = 0.8)
    y "You're drinking bitter warm water again?"
    hide emi_neutral 
    show emi_sigh at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)
    e "It's {i}tea{/i}."
    y "Myeah. Whatever {i}you{/i} say."
    y "Don't you have something different? Something more... {i}interesting{/i}?"
    hide yolei_bored 
    hide emi_sigh 

    menu:
        "Do I have a different drink for Yolei?"

        "Bitter warm water only.":
            jump no_yolei_ending 

        "Nope.":
            jump no_yolei_ending 
            
        "Make him drink the potion I found" if bottleKnowledge:
            jump yolei_bald_path


label no_yolei_ending:
    "Failed Yolei ending path."


label yolei_bald_path:
    "Bald Yolei ending"




label craft_path:
    scene emi_room with dissolve
    show screen statButton
    pause 0.3
    #TODO: chang music?
    play music "music/craft_time.mp3" fadein 0.5
    show emi_neutral at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8) with dissolve
    e "{i}I spent the rest of the day thinkering away.{/i}"
    e "{i}Time flew by so quickly, and I made a lot of progress!{/i}"
    hide emi_neutral

    #Ending Picture
    hide screen statButton
    window hide
    pause 0.2
    show craft_ending at Transform(zoom = 0.7) with dissolve:
        truecenter
    pause 2.5
    hide craft_ending

    show screen statButton
    show emi_neutral at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)
    hide emi_neutral
    show emi_happy at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)
    e "{i}Wabee is still a bit wobbly, but he can fly properly now.{/i}"
    voice "voice/emi/emi_laugh2.mp3"
    e "{i}One day, I'm sure I'll be able to make him spit fire!{/i}"
    hide emi_happy
    "Congrats! You've reached the craft ending!"
    "Will you be able to reach Ara's and Yolei's ending too?"
    return
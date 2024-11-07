label start:
    show border onlayer screens
    play music "music/reflexion.mp3" fadein 0.5

    "My mom always made a fuss about my sleeping habits."
    "{i}\"Oh my. You're only waking up now?\"{/i}"
    "{i}\"There's nothing quite like enjoying a nice cup of tea and watching the sun rise.\"{/i}"
    "{i}\"I hope one day, you'll be able to enjoy the nice little things life has to offer.\"{/i}"
    "{i}\"Unlike the complete blockhead of a man I ended up marrying and who calls himself your father--\"{/i}"

    scene workshop with dissolve
    show screen statButton
    pause 0.3
    show emi_neutral at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8) with dissolve
    voice "voice/emi_laugh.mp3"
    e "Indeed, I believe there would be nothing better than to enjoy a quiet peaceful morning..."
    e "Peacefully quietly..."
    e "Starting the day slowly..."

    hide emi_neutral
    stop music fadeout 0.5
    e "... without having to face the consequences of waking up late when the shop was exceptionally open this morning."

    play music "music/tension.mp3" fadein 0.5
    show emi_sad2 at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8) with dissolve
    voice "voice/emi_why_neutral.mp3"
    e "I know it was my fault for opening the shop late, but still..."
    e "Those adventurers didn't have to be so mean."

    hide emi_sad2
    stop music fadeout 0.5
    show emi_annoyed at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)
    e "And it wasn't such a big deal that they had to kick Wabee."
    play music "music/upbeat.mp3" fadein 0.5
    e "{i}Nobody hurts Wabee.{/i}"
    e "{i}Who cares if your dagger is not repaired? I bet that stupid elf cannot aim!{/i}"
    e "{i}Meyfyre... I'll remember you and your stupid friends.{/i}"
    e "..."
    hide emi_annoyed
    show emi_angry at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)
    voice "voice/emi_actually_brat2.mp3"
    e "{i}I hope you and your group get attacked by a bugbear.{/i}"
    e "{i}Assholes.{/i}"
    stop music fadeout 0.5


label path:
    play music "music/eastfall.ogg" fadein 0.5
    scene emi_room with dissolve
    show screen statButton
    pause 0.3
    show emi_sigh at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8) with dissolve
    e "{i}Sigh{/i}. At least they're gone, and I can finally close the shop!"
    hide emi_sigh 
    show emi_smirk at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)
    voice "voice/emi_laugh2.mp3"
    e "I'll have Master Baltazar treat me at the tavern once he's back. That's the least he can do!"
    hide emi_smirk
    show emi_neutral at Transform(xpos = 0.05, ypos = 0.95, anchor = (0.0, 1.0), zoom = 0.8)
    e "Now, what should I do for the rest of the day?"
    hide emi_neutral

    menu:
        "Choose Emi's path."

        #CRAFT PATH
        "Craft the day away.":
            jump craft_path

        #ARA's PATH
        "Take a stroll in the forest.":
            jump ara_path

        #YOLEI'S PATH
        "Is that beer on the kitchen counter??":
            jump yolei_path

            

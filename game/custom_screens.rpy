screen statButton:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "images/misc/dice.png"
        #hover
        action ShowMenu ("emiStats")

screen emiStats:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "images/misc/dice.png"
        #hover
        action Return ()
    frame:
        background Solid("#3498db")
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30
        #box placement
        hbox:
            spacing 40

            vbox:
                spacing 10
                text "Proficency" size 35
                text "Strength" size 35
                text "Dexterity" size 35
                text "Constitution" size 35
                text "Intelligence" size 35
                text "Wisdom" size 35
                text "Charisma" size 35

            vbox:
                spacing 10
                text "[proficency]" size 35
                text "[strength]" size 35
                text "[dexterity]" size 35
                text "[constitution]" size 35
                text "[intelligence]" size 35
                text "[wisdom]" size 35
                text "[charisma]" size 35
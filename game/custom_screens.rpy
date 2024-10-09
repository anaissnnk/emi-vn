# img button to display state on main UI
screen statButton:
    imagebutton:
        xalign 1.0
        yalign 0.07
        xoffset -30
        yoffset 30
        idle "images/misc/stats.png"
        hover "images/misc/stats_hover.png"
        action ShowMenu ("emiStats")

# display the page content related to stats
screen emiStats:
    # set stats bg image
    add "gui/main_menu.png"

    #stats button behavior
    imagebutton:
        xalign 1.0
        yalign 0.07
        xoffset -30
        yoffset 30
        idle "images/misc/stats.png"
        hover "images/misc/stats_hover.png"
        action Return ()

    #frame containing the stats block
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 40
        ypadding 40
        #box placement
        hbox:
            spacing 40

            vbox:
                spacing 10
                text "Proficency" size 30
                text "Strength" size 30
                text "Dexterity" size 30
                text "Constitution" size 30
                text "Intelligence" size 30
                text "Wisdom" size 30
                text "Charisma" size 30

            vbox:
                spacing 10
                text "[proficency]" size 30
                text "[strength]" size 30
                text "[dexterity]" size 30
                text "[constitution]" size 30
                text "[intelligence]" size 30
                text "[wisdom]" size 30
                text "[charisma]" size 30
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Robotnik")
define r = Character("Reiker")
define y = Character("Yanshu")
define p = Character("Prosecutor")

style imgbutton is text:
    color '#000'
    textalign 0.5
    yalign 0.5
    xalign 0.5
# The game starts here.

label start:
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    scene bg back




    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    $ testimonyid = 0
    $ testimonymin = 0
    $ testimonymax = 2


    
    show bg left as bgleft:
        crop (0, 0, 256, 720)
        xpos 0
        ypos 0

    show bg right as bgright:
        crop (1024, 0, 1280, 720)
        xpos 1024
        ypos 0    


        

    show reiker test as courtleft:
       
        xalign 0
        yalign 0.67

    show yanshu test as courtmid:
       
        xalign 0.5
        yalign 0.67

    show prosecutor test as courtright:

        xalign 0.95
        yalign 0.67

    show eggman test as courtjudge:
        xalign 0.5
        ypos -0.15

    show fg bar as barleft:
        xalign 0.20

    show fg bar as barrightt:
        xalign 0.80

    show fg gear as geartl:
        xpos 0.1725
        ypos -0.05
        rotate 0
    #    linear 1.0 rotate 360
    #    repeat

    show fg gear as geartr:
        xpos 0.7375
        ypos -0.05
        rotate 0
    #    linear 1.0 rotate -360
    #    repeat

    show fg gear as gearbl:
        xpos 0.1725
        ypos 0.685
        rotate 0
    #    linear 1.0 rotate -360
    #    repeat

    show fg gear as gearbr:
        xpos 0.7375
        ypos 0.685
        rotate 0
    #    linear 1.0 rotate 360
    #   repeat
label courtfirsthalf:
    e "We now convene for the trial of Yanshu Driver the Mole. I trust the prosecution is ready to commence?"
label logic:
    screen noAdvance():
        zorder 100
        modal True
 
    screen buttonLeft():
        zorder 101
        fixed:
            xpos 8 ypos 656
            imagebutton:
                idle "buttonleftidle"
                hover "buttonlefthover"
                action Jump("logicleft")
    screen buttonRight():
        zorder 101
        fixed:
            xpos 1062 ypos 656
            imagebutton:
                idle "buttonrightidle"
                hover "buttonrighthover"
                action Jump("logicright")
    screen buttonCallout():
        zorder 101
        fixed:
            xpos 8 ypos 583
            button:
                xsize 211
                ysize 55
                idle_background "buttonidle"
                hover_background "buttonhover"
                action Jump("logicpress")
                text "Press" style "imgbutton"
    screen buttonPresent():
        zorder 101
        fixed:
            xpos 1062 ypos 583
            button:
                xsize 211
                ysize 55
                idle_background "buttonidle"
                hover_background "buttonhover"
                action Jump("logicpresent")
                text "Present" style "imgbutton"
    screen buttonInventory():
        fixed:
            xpos 8
            ypos 8
            button:
                xsize 211
                ysize 55
                idle_background "buttonidle"
                hover_background "buttonhover"
                action Jump("logicinventory")
                text "Inventory" style "imgbutton"

label logicleft:
    $ testimonyid = testimonyid - 1
    jump printing

label logicright:
    $ testimonyid = testimonyid + 1
    jump printing

label logicpress:
    hide screen noAdvance
    hide screen buttonLeft
    hide screen buttonRight
    hide screen buttonCallout
    hide screen buttonPresent
    hide screen buttonInventory

    if testimonyid == 0:
        "Press line 1?"
        e "Press line 1!"
        jump printing
    if testimonyid == 1:
        "Press line 2?"
        e "Press line 2!"
        jump printing
    if testimonyid == 2:
        $ testimonymax = 3
        "Press line 3?"
        e "Press line 3!"
        jump printing
        
    if testimonyid == 3:
        "Press line 4?"
        e "Press line 4!"
        jump printing

label logicpresent:
    hide screen noAdvance
    hide screen buttonLeft
    hide screen buttonRight
    hide screen buttonCallout
    hide screen buttonPresent
    hide screen buttonInventory
    menu evidence:
        "Evidence to use"

        "Evidence 1":
            jump wrongevidence
        "Evidence 2":
            jump wrongevidence
        "Evidence 3":
            jump rightevidence
        "Back":
            jump printing

label rightevidence:
    if testimonyid == 3:
        "you did the thing"
        e "oh noes im dead"
        jump ending
    else:
        jump wrongevidence

label wrongevidence:
    "you did the thing"
    e "nuh uh"
    "piss"
    jump printing

label logicinventory:
    hide screen noAdvance
    hide screen buttonLeft
    hide screen buttonRight
    hide screen buttonCallout
    hide screen buttonPresent
    hide screen buttonInventory
    menu inventory:
        "Evidence to use"

        "Evidence 1":
            jump item1
        "Evidence 2":
            jump item2
        "Evidence 3":
            jump item3
        "Back":
            jump printing

label item1:
    show screen noAdvance
    show ev him:
        xpos -256
        yalign 0.2
        linear 0.5 xalign 0.2 yalign 0.2
        pause 0.5
        linear 0.5 xalign -0.3 yalign 0.2
    hide screen noAdvance
    "who is this"
    hide ev him
    jump printing
label item2:
    show screen noAdvance
    show ev photo:
        xpos -256
        yalign 0.2
        linear 0.5 xalign 0.2 yalign 0.2
        pause 0.5
        linear 0.5 xalign -0.3 yalign 0.2
    hide screen noAdvance
    "a photo"
    hide ev photo
    jump printing
label item3:
    show screen noAdvance
    show ev document:
        xpos -256
        yalign .2
        linear 0.5 xalign 0.2 yalign 0.2
        pause 0.5
        linear 0.5 xalign -0.3 yalign 0.2
    hide screen noAdvance
    "a document"
    hide ev document
    
    jump printing
label printing:
    show screen noAdvance
    show screen buttonLeft
    show screen buttonRight
    show screen buttonCallout
    show screen buttonPresent
    show screen buttonInventory
    if testimonymin > testimonyid:
        $ testimonyid = 0

    if testimonymax < testimonyid:
        $ testimonyid = 0

    # These display lines of dialogue.
    if testimonyid == 0:
        e "Line 1"
        jump logic
    if testimonyid == 1:
        e "Line 2"
        jump logic
    if testimonyid == 2:
        e "Line 3"
        jump logic
    if testimonyid == 3:
        e "Line 4"
        jump logic
    # This ends the game.

label ending:
    return

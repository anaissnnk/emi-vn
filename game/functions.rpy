init python:
    # Intelligence check
    def intelligence_check(intelligence):
        dice_roll = renpy.random.randint(1, 20)
        total = dice_roll + intelligence
        return dice_roll, total

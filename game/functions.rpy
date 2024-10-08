# REGULAR CHECKS
# intelligence check
init python:
    def intelligence_check(intelligence):
        dice_roll = renpy.random.randint(1, 20)
        total = dice_roll + intelligence
        return dice_roll, total

# strength check
init python:
    def strength_check(strength):
        dice_roll = renpy.random.randint(1, 20)
        total = dice_roll + strength
        return dice_roll, total

# dexterity check
init python:
    def dexterity_check(dexterity):
        dice_roll = renpy.random.randint(1, 20)
        total = dice_roll + dexterity
        return dice_roll, total

# constitution check
init python:
    def constitution_check(constitution):
        dice_roll = renpy.random.randint(1, 20)
        total = dice_roll + constitution
        return dice_roll, total

# wisdom check
init python:
    def constitution_check(wisdom):
        dice_roll = renpy.random.randint(1, 20)
        total = dice_roll + wisdom
        return dice_roll, total

# charisma check
init python:
    def charisma_check(charisma):
        dice_roll = renpy.random.randint(1, 20)
        total = dice_roll + charisma
        return dice_roll, total

# PROFICENCY
# nature, arcana, religion check
init python:
    def intelligence_proficency_check(intelligence, proficency):
        dice_roll = renpy.random.randint(1, 20)
        total = dice_roll + intelligence + proficency
        return dice_roll, total

# sleight of hand check
init python:
    def dexterity_proficency_check(dexterity, proficency):
        dice_roll = renpy.random.randint(1, 20)
        total = dice_roll + dexterity + proficency
        return dice_roll, total

# EXPERTISE
# investigation
init python:
    def intelligence_expertise_check (intelligence, expertise):
        dice_roll = renpy.random.randint(1, 20)
        total = dice_roll + intelligence + expertise
        return dice_roll, total

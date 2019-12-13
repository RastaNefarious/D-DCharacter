#!/usr/bin/env python
# coding: utf-8

# In[4]:


from my_modules import my_functions as fn
from my_modules import test_functions
import random
import string

"""
Creating the races and classes from which we will be using to 
create our random characters. There have been many additions of 
races/classes within the years to D&D but for the purposes of 
this we will stick with the basic OG choices
"""
RACES = ['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'Halfling', 'Half-Elf', 
            'Half-Orc', 'Human', 'Tiefling']
CLASSES = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 
        'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']

"""
Putting this outside of our functions first so we can make more 
customizations later on with the different race bonuses, hit die, etc.
"""
CHOOSE_RACE = random.choice(RACES)
CHOOSE_CLASS = random.choice(CLASSES)

"""
There's nine alignments of morality in D&D
"""
ALIGNMENT_LIST = ['Lawful Good', 'Neutral Good', 'Chaotic Good', 
                        'Lawful Neutral', 'Neutral', 'Chaotic Neutral', 
                        'Lawful Evil', 'Neutral Evil', 'Chaotic Evil']

class SpawnCharacter():

    """
    Spawn a character!
    """
    
    def main():
        fn.name()
        fn.alignment(ALIGNMENT_LIST)
        fn.character_race(CHOOSE_RACE)
        fn.character_class(CHOOSE_CLASS)
        fn.hit_points(CHOOSE_CLASS)
        fn.ability_scores(CHOOSE_RACE)
    
    main()


# In[ ]:





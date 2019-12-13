#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from my_modules import my_functions as fn
import string
import random

example_list = ['dominate']
example_list_two = ['Barbarian']
example_string = random.choice(example_list_two)

def test_alignment():
    assert alignment(example_list) == 'dominate'
    
def test_hit_points():
    assert hit_points(example_string) == '22'


# In[ ]:





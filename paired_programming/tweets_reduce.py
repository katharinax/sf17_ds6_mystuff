#!/usr/bin/env python
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
import pprint
import sys
import json


# In[18]:

# fake_file = "JennZimm72\t1 \nJennZimm72\t1 \nrandomstuff\t1"
# for line in fake_file.split("\n"):
#     print(line)


# In[19]:

current_word = None
current_count = 0
word = None

for line in sys.stdin: #fake_file.split("\n"):
    word, count = line.split('\t')
    count = int(count)
    if word == current_word:
        current_count += count
    else:
        if current_word:
            print('{}\t{}'.format(current_word, current_count))
        current_word = word
        current_count = count

if current_word == word:
    print('%s\t%i' % (current_word, current_count))


# In[ ]:

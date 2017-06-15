#!/usr/bin/env python
# coding: utf-8

# In[56]:

import numpy as np
import pandas as pd
import pprint
import sys
import json


# In[59]:

for line in sys.stdin:
    try:
        username = eval(line)['user']['screen_name']
        # pprint.pprint(username)
        print("{}\t{}".format(username, 1))
    except:
        pass


# In[61]:

with open('input.txt') as f:
    for line in f.readlines():
        try:
            username = eval(line)['user']['screen_name']
            # pprint.pprint(username)
            print("{}\t{}".format(username, 1))
        except:
            pass


# In[ ]:

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 17:29:30 2019

@author: jlee
"""


import numpy as np
import os

import init_cfg as ic


# ----- File names ----- #
scr1 = 'comb_daophot1.scr'
# ---------------------- #

import time
start_time = time.time()


# ----- Writing scr1 ----- #
cmname = 'comb'
apname = cmname+'.ap'
cooname = cmname+'.coo'

os.system('rm -rfv '+apname+' '+cooname)

f = open(scr1, 'w')
f.write('attach '+cmname+'\n')
f.write('find'+'\n')
f.write('{0:d},{1:d}'.format(np.sum(ic.nframe), 1)+'\n')
f.write('\n')
f.write('N'+'\n')
f.write('1.0'+'\n')
f.write('\n')
f.write('\n')
f.write('Y'+'\n')
f.write('phot'+'\n')
f.write('\n')
f.write('\n')
f.write('\n')
f.write('\n')
f.write('exit')
f.close()

os.system('daophot < '+scr1)
# ------------------------ #


# Printing the running time
print("--- {0:.1f} seconds ---".format(time.time() - start_time))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 1 21:49:22 2019

@author: jlee
"""


import numpy as np
import os

import init_cfg as ic


# ----- File names ----- #
scr1 = 'comb_daophot2.scr'
# ---------------------- #

import time
start_time = time.time()


# ----- Moving PSFs to other backup directory ----- #
os.system('mkdir PSFs')
os.system('mv -v *.psf PSFs/')
# ------------------------------------------------- #


# ----- Writing scr1 ----- #
cmname = 'comb'
cooname = cmname+'.coo'

for i in np.arange(len(ic.nfits)):
    fname = ic.nfits[i].split('.fits')[0]
    ap2name = fname+'.ap2'

    os.system('rm -rfv '+ap2name)

    f = open(scr1, 'w')
    f.write('attach '+fname+'\n')
    f.write('phot'+'\n')
    f.write('\n')
    f.write('\n')
    f.write(cooname+'\n')
    f.write(ap2name+'\n')
    f.write('exit')
    f.close()

    os.system('daophot < '+scr1)
# ------------------------ #


# Printing the running time
print("--- {0:.1f} seconds ---".format(time.time() - start_time))

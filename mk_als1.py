#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 1 18:52:45 2019

@author: jlee
"""


import numpy as np
import os

import init_cfg as ic


# ----- File names ----- #
scr1 = 'allstar1.scr'
# ---------------------- #

import time
start_time = time.time()


# ----- Writing scr1 and running ----- #
cmname = 'comb'
apname = cmname+'.ap'

for j in np.arange(len(ic.nfits)):
    fname = ic.nfits[j].split('.fits')[0]
    psfname = fname+'.psf'
    alsname = fname+'.als'
    subname = fname+'s.fits'

    os.system('rm -rfv '+alsname+' '+subname)

    print("\n")
    print("Starting the process for "+fname)
    print("\n")
    
    # ----- Writing scr1 ----- #
    f = open(scr1, 'w')
    f.write('\n')
    f.write(fname+'\n')
    f.write(psfname+'\n')
    f.write(apname+'\n')
    f.write(alsname+'\n')
    f.write(subname+'\n')
    f.close()

    os.system('allstar < '+scr1)
    # ------------------------ #

# Printing the running time
print("--- {0:.1f} seconds ---".format(time.time() - start_time))

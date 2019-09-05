#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 18:01:18 2019

@author: jlee
"""


import numpy as np
import os

import init_cfg as ic

import time
start_time = time.time()


# ----- File names ----- #
scr1 = 'daophot1.scr'
# ---------------------- #


# ----- Writing scr1 ----- #
for i in np.arange(len(ic.nfits)):
    fname = ic.nfits[i].split('.fits')[0]
    apname = fname+'.ap'
    cooname = fname+'.coo'
    lstname = fname+'.lst'
    psfname = fname+'.psf'
    neiname = fname+'.nei'
    os.system('rm -rfv '+apname+' '+cooname+' '+lstname+' '+psfname+' '+neiname)

    f = open(scr1, 'w')
    f.write('attach '+fname+'\n')
    f.write('find'+'\n')
    f.write('{0:d},{1:d}'.format(ic.nframe[i], 1)+'\n')
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
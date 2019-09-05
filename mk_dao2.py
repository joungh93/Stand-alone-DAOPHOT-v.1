#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 17:05:30 2019

@author: jlee
"""


import numpy as np
import os
import pandas as pd

import init_cfg as ic


# ----- File names ----- #
scr2 = 'daophot2.scr'
# ---------------------- #

import time
start_time = time.time()

# ----- Writing scr2 and running ----- #
for j in np.arange(len(ic.nfits)):
    fname = ic.nfits[j].split('.fits')[0]
    cooname = fname+'.coo'
    neiname = fname+'.nei'
    psfname = fname+'.psf'
    lstname = fname+'.lst'

    os.system('rm -rfv '+neiname+' '+psfname)

#%%
    print("\n")
    print("Starting the process for "+fname)
    print("\n")

    # ----- Writing scr2 ----- #
    f = open(scr2, 'w')
    f.write('attach '+fname+'\n')
    f.write('psf'+'\n')
    f.write('\n')
    f.write('\n')
    f.write('\n')
    f.write('exit')
    f.close()

    os.system('daophot < '+scr2)
    # ------------------------ #

    # Iterations
    n_iter = 1
    while True:
        it = input("Do you want to iterate again? (Y/N) : ")
        if (it == 'N'):
            print("Finishing the iterations...")
            break
        if ((it != 'Y') & (it != 'N')):
            print("Please type only Y or N!")
            TypeError
        if (it == 'Y'):
            print("Continuing the iterations...")
            
            dat_nei = pd.read_fwf(neiname, dtype=None, header=None, skiprows=3)
            subtract = ((dat_nei[5] == '?') | (dat_nei[5] == '*'))
            id_subtract = dat_nei.loc[subtract, 0].values
            
            dat_lst = pd.read_fwf(lstname, dtype=None, header=None, skiprows=3)
            os.system('rm -rfv '+neiname+' '+psfname)
            
            # Making *.lst file
            g = open(cooname,'r')
            line1 = g.readline()
            line2 = g.readline()
            line2 = line2.replace("  1  ", "  3  ", 1)
           
            f = open(lstname, 'w')
            f.write(line1)
            f.write(line2)
            f.write('\n')
            for i in np.arange(len(dat_lst)):
                if (dat_lst[0].values[i] in id_subtract):
                    continue
                else:
                    f.write(' {0:7d}  {1:8.2f}  {2:8.2f}  {3:6.3f}  {4:6.3f}'.format(dat_lst[0].values[i], dat_lst[1].values[i], dat_lst[2].values[i], dat_lst[3].values[i], dat_lst[4].values[i])+'\n')
            f.close()
            
            os.system('daophot < '+scr2)
            n_iter += 1
# ------------------------------------ #       


# Printing total number of iteration
print("Total # of iterations : {0:d}".format(n_iter))


# Printing the running time
print("--- {0:.1f} seconds ---".format(time.time() - start_time))


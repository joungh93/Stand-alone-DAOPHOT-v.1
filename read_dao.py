#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 3 15:10:32 2019

@author: jlee
"""


import time
start_time = time.time()

import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import pandas as pd
import os

import init_cfg as ic


# Magnitude factors
magfac = 2.0 + 2.5*np.log10(ic.ifac)


# Declaration of columns
magname = []
for i in np.arange(ic.nmag):
    magname += ['mag{0:d}'.format(i+1)]
    
merrname = []
for i in np.arange(ic.nmag):
    merrname += ['merr{0:d}'.format(i+1)]

colname1 = ['id','x','y'] + magname
colname2 = ['sky','skysig','skyskew'] + merrname
colname3 = ['id','x','y','mag','merr','sky','niter','chi','sharp']


# Reading data from *.als *.ap2 files
for j in np.arange(len(ic.nfits)):
    fname = ic.nfits[j].split('.fits')[0]
    ap2name = fname+'.ap2'
    alsname = fname+'.als'    

    dat_ap = np.genfromtxt(ap2name, dtype=None, encoding='ascii', skip_header=4)
    df_ap1 = pd.DataFrame(dat_ap[0::2], columns=colname1)
    df_ap2 = pd.DataFrame(dat_ap[1::2], columns=colname2)
    exec(fname+'_ap2 = pd.concat([df_ap1, df_ap2], axis=1)')

    dat_als = np.genfromtxt(alsname, dtype=None, encoding='ascii', skip_header=3,
                            names=colname3)
    exec(fname+'_als = pd.DataFrame(dat_als)')

    exec(fname+'_ap2.to_pickle("./'+fname+'_ap2.pkl")')
    exec(fname+'_als.to_pickle("./'+fname+'_als.pkl")')


# Printing the running time
print("--- {0:.1f} seconds ---".format(time.time() - start_time))
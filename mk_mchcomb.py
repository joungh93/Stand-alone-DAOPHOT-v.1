#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 21:14:35 2019

@author: jlee
"""


import numpy as np
import os
from astropy.io import fits

from pyraf import iraf
iraf.images()
iraf.immatch()

import init_cfg as ic

import time
start_time = time.time()


# ----- Setting the reference image ----- #
img_filt = np.array([ic.nfits[i][0] for i in np.arange(len(ic.nfits))])
ref = (img_filt == ic.ref_filt)


# ----- Making lists of non-reference images ----- #
noref_list = ' '
for i in np.arange(np.sum(~ref)):
    noref_list += np.array(ic.nfits)[~ref][i]+' '
os.system('ls -1'+noref_list+'> inp.lis')

f = open('ker.lis','w')
for i in np.arange(np.sum(~ref)):
    f.write('ker_'+np.array(ic.nfits)[~ref][i]+'\n')
f.close()


# ----- Making PSF-matched & combining them ----- #
os.system('rm -rfv '+'comb.fits')
for i in np.arange(np.sum(~ref)):
    os.system('rm -rfv '+'m'+np.array(ic.nfits)[~ref][i])
for i in np.arange(np.sum(~ref)):
    os.system('rm -rfv '+'ker_'+np.array(ic.nfits)[~ref][i])

try:
    iraf.psfmatch(input='@inp.lis', referenc=np.array(ic.nfits)[ref][0],
                  psfdata=np.array(ic.nfits)[ref][0].split('.')[0]+'_psf.reg',
                  kernel='@ker.lis', output='m//@inp.lis', convolu='image',
                  dnx=31, dny=31, pnx=15, pny=15)

    for i in np.arange(np.sum(~ref)):
        if (i == 0):
            dat_noref = fits.getdata('m'+np.array(ic.nfits)[~ref][i])
        else:
            dat_noref += fits.getdata('m'+np.array(ic.nfits)[~ref][i])
    dat_ref = fits.getdata(np.array(ic.nfits)[ref][0])
    
    fits.writeto('comb.fits', (dat_noref+dat_ref)/3.0, overwrite=True)

except:
    for i in np.arange(np.sum(~ref)):
        if (i == 0):
            dat_noref = fits.getdata(np.array(ic.nfits)[~ref][i])
        else:
            dat_noref += fits.getdata(np.array(ic.nfits)[~ref][i])
    dat_ref = fits.getdata(np.array(ic.nfits)[ref][0])
    
    fits.writeto('comb.fits', (dat_noref+dat_ref)/3.0, overwrite=True)


# Printing the running time
print("--- {0:.1f} seconds ---".format(time.time() - start_time))


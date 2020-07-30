#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 13:41:27 2019

@author: jlee
"""


import time
start_time = time.time()

import numpy as np
from astropy.io import fits
import os

import init_cfg as ic


# ----- Making new FITS files for running DAOPHOT ----- #
for i in np.arange(len(ic.ifits)):
    print("Reading "+ic.ifits[i].split('/')[-1]+" ...")
    dat, hdr = fits.getdata(ic.ifits[i], extn=ic.num_ext0, header=True)
    dat = dat.astype('float32')
    fits.writeto(ic.nfits[i], ic.sky_off+ic.ifac*dat/ic.itime[i], hdr, overwrite=True)


# ----- Writing opt files ----- #

# opt1
f = open(ic.opt1, 'w')
f.write(f"RE = {ic.readn:.2f}\n")
f.write(f"GA = {ic.gain:.2f}\n")
f.write(f"LO = {ic.lo:.2f}\n")    # Low good datum (sigma)
f.write(f"HI = {ic.hi:.2f}\n")    # High good datum (ADU)
f.write(f"FW = {ic.fw:.2f}\n")
f.write(f"TH = {ic.th:.2f}\n")
f.write(f"LS = 0.20\n")    # low sharpness cutoff
f.write(f"HS = 1.00\n")    # high sharpness cutoff
f.write(f"LR = -1.00\n")    # low roundness cutoff
f.write(f"HR = 1.00\n")    # high roundness cutoff
f.write(f"WA = -2.00\n")    # watch process
f.write(f"FI = {ic.fi:.2f}\n")
f.write(f"PS = {ic.ps:.2f}\n")
f.write(f"VA = 2.00\n")    # variable PSF
f.write(f"AN = 6.00\n")    # analytic model PSF
f.write(f"EX = 5.00\n")    # extra PSF cleaning passes
f.write(f"PE = 0.75\n")    # percent error (%)
f.write(f"PR = 5.00\n")    # profile error (%)
f.close()

# opt 2
f = open(ic.opt2, 'w')
for i in np.arange(ic.nmag):
	f.write(f"A{i+1:d} = {ic.ap[i]:.3f}\n")
f.write(f"IS = {ic.in_sky:.3f}\n")
f.write(f"OS = {ic.out_sky:.3f}\n")
f.close()

# opt3
f = open(ic.opt3, 'w')
f.write(f"FI = {ic.fi:.2f}\n")
f.write(f"CE = {ic.ce3:.2f}\n")
f.write(f"RE = 1.0\n")
f.write(f"CR = 2.5\n")
f.write(f"WA = {ic.wa3:.2f}\n")
f.write(f"MA = 50.0\n")
f.write(f"PE = 0.75\n")
f.write(f"PR = 5.00\n")
f.write(f"IS = {ic.in_sky:.2f}\n")
f.write(f"OS = {ic.out_sky:.2f}\n")
f.close()

# opt4
f = open(ic.opt4, 'w')
f.write(f"CE = {ic.ce4:.2f}\n")
f.write(f"CR = {ic.cr:.2f}\n")
f.write(f"GE = {ic.ge:.2f}\n")
f.write(f"WA = {ic.wa4:.2f}\n")
f.write(f"MI = {ic.mi:.2f}\n")
f.write(f"MA = {ic.ma:.2f}\n")
f.write(f"PE = 0.00\n")
f.write(f"PR = 0.00\n")
f.write(f"IS = {ic.in_sky:.2f}\n")
f.write(f"OS = {ic.out_sky:.2f}\n")
f.close()


# Printing the running time
print("--- {0:.1f} seconds ---".format(time.time() - start_time))
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


for i in np.arange(len(ic.ifits)):
    dat, hdr = fits.getdata(ic.diI+ic.ifits[i], extn=1, header=True)
    dat = dat.astype('float32')
    fits.writeto(ic.nfits[i], ic.sky_off+ic.ifac*dat/ic.expt[i], hdr, overwrite=True)


# Printing the running time
print("--- {0:.1f} seconds ---".format(time.time() - start_time))
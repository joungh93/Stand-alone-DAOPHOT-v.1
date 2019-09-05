#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 21:26:37 2019

@author: jlee
"""


import numpy as np
import os
from time import sleep

from pyraf import iraf
iraf.images()
iraf.tv()

import init_cfg as ic


com_ds9 = 'ds9 -scalemode zscale -scale lock yes -frame lock image '

# ----- Enter an image list (manually!) ----- #
# imglist = ' '
# for i in np.arange(len(ic.nfits)):
#     imglist += ic.nfits[i]+' '

imgs = ['B.fits','mB.fits','V.fits']
imglist = ' '
for i in np.arange(len(imgs)):
    imglist += imgs[i]+' '

# ------------------------------------------- #

os.system(com_ds9+imglist+'&')
sleep(float(len(ic.nfits)))
iraf.imexamine()



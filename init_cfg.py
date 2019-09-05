#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 13:41:27 2019

@author: jlee
"""

# File structure declaration
diI = './Images/'
diO = './alipy_out/'

# ifits : initial FITS file names
ifits = ['calexp-HSC-G-0-6,2.fits',
         'calexp-HSC-R-0-6,2.fits',
         'calexp-HSC-I-0-6,2.fits']
expt = [1.0, 1.0, 1.0]
# ali_ref = 'n2041v.fits'

# # afits : alipy_out images
# afits = ['n2041b_gregister.fits', 'n2041v_gregister.fits']

# nfits : new FITS file names
nfits = ['G0-6x2.fits', 'R0-6x2.fits', 'I0-6x2.fits']
sky_off = 100.0    # a sky offset value
ifac = 100.0    # an image multiplying factor

# Number of frames (average, sum)
nframe = [16, 13, 13]

# Number of apertures for DAOPHOT
nmag = 7

# Setting for plotting
maglab = ['HSC-G', 'HSC-R', 'HSC-I']    # Magnitude labels
xran = [15.0,29.0]
xtic = list(range(16, 32, 2))

# Reference filter
ref_filt = 'I'
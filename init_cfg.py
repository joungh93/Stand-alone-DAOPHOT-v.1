#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 13:41:27 2019

@author: jlee
"""


import glob, os


# ----- Initial images ----- #
diI = '../Images/'    # Initial image directory
ifits = glob.glob(diI+'*.fits')    # Initial images
ifits = sorted(ifits)
itime = [1.0]*len(ifits)    # Image exposure time (if the images are normalized)
ifilt = [k.split('/')[-1].split('-')[2] for k in ifits]    # Image filters
num_ext0 = 1    # The extension number we should read


# ----- Output images ----- #
sky_off = 100.0    # A sky offset value
ifac = 100.0    # A multifying factor of each image

# The names of new images for running DAOPHOT
nfits = [k.split('/')[-1].split('calexp-HSC-')[1].replace(',','x') for k in ifits]


# ----- DAOPHOT task ----- #
nframe = [16, 13, 13]    # Number of frames (average, sum)
nmag = 7    # Number of apertures

# File names
opt1 = 'daophot.opt'
opt2 = 'photo.opt'
opt3 = 'allstar.opt'
opt4 = 'allframe.opt'

# Initial parameters for opt1
readn = 4.5    # Read noise (ADU; 1 frame)
gain = 3.0    # Gain (e-/ADU; 1 frame)
fw = 4.0    # FWHM
th = 3.0    # Threshold (sigma)
fi = 4.0    # Fitting radius
ps = 12.0    # PSF radius
lo = 15.0    # Low good datum (sigma)
hi = 70000.0    # High good datum (ADU)

# Initial parameters for opt2
ap = [2.0, 3.0, 4.0, 5.0, 6.0, 9.0, 12.0]    # Radii of aperture (the length must be the same as nmag!)
in_sky = 20.0    # Innter sky radius
out_sky = 40.0    # Outer sky radius

# Initial parameters for opt3
ce3 = 6.0    # clipping exponent
re = 1.0    # redetermine centroids
wa3 = 0.0    # watch progress

# nitial parameters for opt4
ce4 = 2.0    # clipping exponent
cr = 2.5    # clipping range
ge = 20.0    # geometric coefficients
wa4 = 0.0    # watch progress
mi = 5.0    # minimum iterations
ma = 100.0    # maximum iterations


# ----- Plotting ----- #
maglab = ['HSC-'+i for i in ifilt]    # Magnitude labels
xran = [15.0,29.0]    # Magnitude range
xtic = list(range(16, 32, 2))    # Magnitude ticks
magfac = 2.0 + 2.5*np.log10(ifac)    # Magnitude factor
m_lcut, m_hcut = 17.5, 21.5    # Magnitude range
C_lcut, C_hcut = 0.25, 0.35    # Concentration index range


# ----- PSFMATCH ----- #
ref_filt = 'I'    # Reference filter
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 18:01:18 2019

@author: jlee
"""


import numpy as np
import os


# ----- File names ----- #
opt1 = 'daophot.opt'
opt2 = 'photo.opt'
opt3 = 'allstar.opt'
opt4 = 'allframe.opt'
# ---------------------- #


# ----- Initial parameters for opt1 ----- #
readn = 4.5    # read noise (ADU; 1 frame)
gain = 3.0    # gain (e-/ADU; 1 frame)
fw = 4.0    # FWHM
th = 3.0    # threshold (sigma)
fi = 4.0    # fitting radius
ps = 12.0    # PSF radius
lo = 15.0    # Low good datum (sigma)
hi = 70000.0    # High good datum (ADU)
# --------------------------------------- #

# ----- Initial parameters for opt2 ----- #
ap1 = 2.0    # Radius of aperture 1
ap2 = 3.0
ap3 = 4.0
ap4 = 5.0
ap5 = 6.0
ap6 = 9.0
ap7 = 12.0
in_sky = 20.0    # innter sky radius
out_sky = 40.0    # outer sky radius
# --------------------------------------- #

# ----- Initial parameters for opt3 ----- #
fi = 4.0    # fitting radius
ce3 = 6.0    # clipping exponent
re = 1.0    # redetermine centroids
wa3 = 0.0    # watch progress
in_sky = 20.0    # innter sky radius
out_sky = 40.0    # outer sky radius
# --------------------------------------- #

# ----- Initial parameters for opt4 ----- #
ce4 = 2.0    # clipping exponent
cr = 2.5    # clipping range
ge = 20.0    # geometric coefficients
wa4 = 0.0    # watch progress
mi = 5.0    # minimum iterations
ma = 100.0    # maximum iterations
in_sky = 20.0    # innter sky radius
out_sky = 40.0    # outer sky radius
# --------------------------------------- #

#%%

# ----- Writing opt1 ----- #
f = open(opt1, 'w')
f.write('RE = {0:.2f}'.format(readn)+'\n')
f.write('GA = {0:.2f}'.format(gain)+'\n')
f.write('LO = {0:.2f}'.format(lo)+'\n')    # Low good datum (sigma)
f.write('HI = {0:.2f}'.format(hi)+'\n')    # High good datum (ADU)
f.write('FW = {0:.2f}'.format(fw)+'\n')
f.write('TH = {0:.2f}'.format(th)+'\n')
f.write('LS = {0:.2f}'.format(0.20)+'\n')    # low sharpness cutoff
f.write('HS = {0:.2f}'.format(1.00)+'\n')    # high sharpness cutoff
f.write('LR = {0:.2f}'.format(-1.00)+'\n')    # low roundness cutoff
f.write('HR = {0:.2f}'.format(1.00)+'\n')    # high roundness cutoff
f.write('WA = {0:.2f}'.format(-2.00)+'\n')    # watch process
f.write('FI = {0:.2f}'.format(fi)+'\n')
f.write('PS = {0:.2f}'.format(ps)+'\n')
f.write('VA = {0:.2f}'.format(2.00)+'\n')    # variable PSF
f.write('AN = {0:.2f}'.format(6.00)+'\n')    # analytic model PSF
f.write('EX = {0:.2f}'.format(5.00)+'\n')    # extra PSF cleaning passes
f.write('PE = {0:.2f}'.format(0.75)+'\n')    # percent error (%)
f.write('PR = {0:.2f}'.format(5.00)+'\n')    # profile error (%)
f.close()
# ------------------------ #

# ----- Writing opt2 ----- #
f = open(opt2, 'w')
f.write('A1 = {0:.3f}'.format(ap1)+'\n')
f.write('A2 = {0:.3f}'.format(ap2)+'\n')
f.write('A3 = {0:.3f}'.format(ap3)+'\n')
f.write('A4 = {0:.3f}'.format(ap4)+'\n')
f.write('A5 = {0:.3f}'.format(ap5)+'\n')
f.write('A6 = {0:.3f}'.format(ap6)+'\n')
f.write('A7 = {0:.3f}'.format(ap7)+'\n')
f.write('IS = {0:.3f}'.format(in_sky)+'\n')
f.write('OS = {0:.3f}'.format(out_sky)+'\n')
f.close()
# ------------------------ #

# ----- Writing opt3 ----- #
f = open(opt3, 'w')
f.write('FI = {0:.2f}'.format(fi)+'\n')
f.write('CE = {0:.2f}'.format(ce3)+'\n')
f.write('RE = {0:.2f}'.format(1.0)+'\n')
f.write('CR = {0:.2f}'.format(2.5)+'\n')
f.write('WA = {0:.2f}'.format(wa3)+'\n')
f.write('MA = {0:.2f}'.format(50.0)+'\n')
f.write('PE = {0:.2f}'.format(0.75)+'\n')
f.write('PR = {0:.2f}'.format(5.00)+'\n')
f.write('IS = {0:.2f}'.format(in_sky)+'\n')
f.write('OS = {0:.2f}'.format(out_sky)+'\n')
f.close()
# ------------------------ #

# ----- Writing opt4 ----- #
f = open(opt4, 'w')
f.write('CE = {0:.2f}'.format(ce4)+'\n')
f.write('CR = {0:.2f}'.format(cr)+'\n')
f.write('GE = {0:.2f}'.format(ge)+'\n')
f.write('WA = {0:.2f}'.format(wa4)+'\n')
f.write('MI = {0:.2f}'.format(mi)+'\n')
f.write('MA = {0:.2f}'.format(ma)+'\n')
f.write('PE = {0:.2f}'.format(0.0)+'\n')
f.write('PR = {0:.2f}'.format(0.0)+'\n')
f.write('IS = {0:.2f}'.format(in_sky)+'\n')
f.write('OS = {0:.2f}'.format(out_sky)+'\n')
f.close()
# ------------------------ #




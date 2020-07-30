# pyDAOPHOT-v.1
(updated on 2020. 07. 30.)


## Description
Test codes for automatically running PSF photometry using the stand-alone version of [DAOPHOT II: The Next Generation](http://www.astro.wisc.edu/sirtf/daophot2.pdf).


(revising...)


## Test images
A patch (6,2) out of M81 HSC gri images ('M81_1' field)

## Initialization
rm -rfv PSFs

rm -rfv *.opt *.scr *.lis *.coo *.ap* *.png *.psf *.nei *.lst *.als *s.fits

## Prerequisites
init_cfg.py    # Initial configurations

alip_img.py    # Aligning images w/ the Alipy 2.0 package (only if needed!)

## Workflow
mk_fits.py    # Making single extension FITS files by adding/multiplying pixel counts

mk_opt.py    # Making *.opt files

mk_dao1.py    # Making a script for running the 1st DAOPHOT step

plt_check1.py    # The 1st check for selecting PSF stars

mk_dao2.py    # Making a script for running the 2nd DAOPHOT step

mk_mchcomb.py    # Making PSF-matched & combined images

mkcm_dao1.py    # Running the 1st DAOPHOT step for the combined image

mk_als1.py    # Making the 1st ALLSTAR step for each image w/ coordinates from the combined image

mkcm_dao2.py    # Making the 2nd DAOPHOT step for each image w/ coordinates from the combined image

## Supplements
mk_psf.py    # Making PSF images

view_imex.py    # Running IRAF/imexamine interactive task

read_dao.py

## Working environments
ipython / spyder (python 3.7)

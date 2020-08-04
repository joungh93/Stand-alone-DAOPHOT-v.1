#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 04 10:58:42 2020

@author: jlee
"""


import os


def run_daophot(image_name, script_name,
                find=True, n_avg=1, n_sum=1, find_again=False, new_thres=1.0,
                phot=True, phot_pos=False, phot_ap=False, phot_pos_name=None, phot_ap_name=None,
                psf=True, psf_ap=False, psf_ap_name=None):

    '''
    image_name: the name of images (dtype: string including '.fits')
    script_name: the name of daophot script (dtype: string)

    find: running find task (dtype: boolean)
    n_avg: if find=True, the number of the averaged frames (default: 1)
    n_sum: if find=True, the numver of the summed frames (default: 1)
    find_again: if find=True, running find task one more time (dtype: boolean)
    new_thres: if find_again=True, the new threshold for finding more sources (default: 1.0)

    phot: running phot task (dtype: boolean)
    phot_pos: if phot=True, using the position file by default or not (dtype: boolean)
    phot_ap: if phot=True, using the magnitude file by default or not (dtype: boolean)
    phot_pos_name: if phot_pos=True, the name of the position file (dtype: string like "*.coo")
    phot_ap_name: if phot_ap=True, the name of the magnitude file (dtype: string like "*.ap")

    psf: running psf task (dtype: boolean)
    psf_ap: if psf=True, using the magnitude file by default or not (dtype: boolean)
    psf_ap_name: if psf_ap=True, the name of the magnitude file (dtype: string like "*.ap")
    '''

    # ----- Initialization ----- #
    fname = image_name.split('.fits')[0]
    apname = fname+'.ap'
    cooname = fname+'.coo'
    lstname = fname+'.lst'
    psfname = fname+'.psf'
    neiname = fname+'.nei'
    os.system('rm -rfv '+apname+' '+cooname+' '+lstname+' '+psfname+' '+neiname)

    # ----- Writing a script file ----- #
    f = open(script_name, 'w')

    # attach task
    f.write("attach "+fname+"\n")

    # find task
    if find:
        f.write("find\n")
        f.write(f"{n_avg:d},{n_sum:d}\n\n")
        if find_again:
            f.write("N\n")
            f.write(f"{new_thres:.2f}\n\n\n")
        f.write("Y\n")

    # phot task
    if phot:
        f.write("phot\n")
        f.write("\n\n")
        if phot_pos:
            f.write(phot_pos_name+"\n")
        else:
            f.write("\n")
        if phot_ap:
            f.write(phot_ap_name+"\n")
        else:
            f.write("\n")

    # psf task
    if psf:
        f.write("psf\n")
        if psf_ap:
            f.write(psf_ap_name+"\n")
        else:
            f.write("\n")
        f.write("\n\n")

    f.write("exit")
    f.close()

    # Running the script
    os.system("daophot < "+script_name)


def run_allstar(image_name, script_name, default_files=True,
                psfname=None, apname=None, alsname=None, subname=None):

    '''
    image_name: the name of images (dtype: string including '.fits')
    script_name: the name of allstar script (dtype: string)

    default_files: if True, using the names of *.psf *.ap *.als *s.fits files by default (dtype: boolean)
    psfname: the name of the psf file (dtype: string like "*.psf")
    apname: the name of the magnitude file (dtype: string like "*.ap")
    alsname: the name of the allstar file (dtype: string like "*.als")
    subname: the name of the subtracted image file (dtype: string like "*s.fits")
    '''

    # ----- Initialization ----- #
    fname = image_name.split('.fits')[0]
    if default_files:
        psfname = fname+".psf"
        apname = fname+".ap"
        alsname = fname+".als"
        subname = fname+"s.fits"

    f = open(script_name, "w")
    f.write("\n")
    f.write(fname+"\n")
    f.write(psfname+"\n")
    f.write(apname+"\n")
    f.write(alsname+"\n")
    f.write(subname+"\n")   
    f.close()

    # Running the script
    os.system("allstar < "+script_name)

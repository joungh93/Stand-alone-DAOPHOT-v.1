#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 04 15:55:58 2020

@author: jlee
"""


import numpy as np
import os
from matplotlib import pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib import ticker
import pandas as pd

import init_cfg as ic
from photpkg import run_daophot

import time
start_time = time.time()


for j in np.arange(len(ic.nfits)):
    fname = ic.nfits[j].split('.fits')[0]
    apname = fname+'.ap'
    cooname = fname+'.coo'
    lstname = fname+'.lst'
    psfname = fname+'.psf'
    neiname = fname+'.nei'
    scr1name = 'daophot1.scr'


    # ----- Running the 1st DAOPHOT task ----- #
    os.system('rm -rfv '+apname+' '+cooname+' '+lstname+' '+psfname+' '+neiname)
    run_daophot(ic.nfits[j], scr1name,
                find=True, n_avg=ic.nframe[j], n_sum=1, find_again=False,
                phot=True, phot_pos=False, phot_ap=False,
                psf=False)

    magname = []
    for i in np.arange(ic.nmag):
        magname += ['mag{0:d}'.format(i+1)]
        
    merrname = []
    for i in np.arange(ic.nmag):
        merrname += ['merr{0:d}'.format(i+1)]

    colname1 = ['id','x','y'] + magname
    colname2 = ['sky','skysig','skyskew'] + merrname

    dat_ap = np.genfromtxt(apname, dtype=None, encoding='ascii', skip_header=4)

    df_ap1 = pd.DataFrame(dat_ap[0::2], columns=colname1)
    df_ap2 = pd.DataFrame(dat_ap[1::2], columns=colname2)
    df_ap = pd.concat([df_ap1, df_ap2], axis=1)


    # Selecting valid data
    str_mcnd = "(df_ap['mag1'] < 99.999)"
    for i in np.arange(1, ic.nmag, 1):
        str_mcnd += ' & '
        str_mcnd += "(df_ap['mag"+'{0:d}'.format(i+1)+"'] < 99.999)"
        
    str_mecnd = "(df_ap['merr1'] < 9.999)"
    for i in np.arange(1, ic.nmag, 1):
        str_mecnd += ' & '
        str_mecnd += "(df_ap['merr"+'{0:d}'.format(i+1)+"'] < 9.999)"

    exec('val = ('+str_mcnd+' & '+str_mecnd+')')

    # Definition
    mag, merr = df_ap['mag3'], df_ap['merr3']
    Ci = df_ap['mag2'] - df_ap['mag4']


    # ----- Plotting & selecting PSF stars ----- #
    print("\n")
    print("Starting to plot for "+ic.maglab[0])
    print("\n")

    n_plt = 0
    while True:

        if (n_plt == 0):
            m_lcut, m_hcut = ic.m_lcut, ic.m_hcut
            C_lcut, C_hcut = ic.C_lcut, ic.C_hcut

        elif (n_plt > 0):
            print("\n")
            it = input("Do you want to plot again? (Y/N): ")

            if (it == 'N'):
                print("Finishing plotting...")
                plt.savefig(fname+'-check1.png', dpi=300)
                plt.close()
                break
            if ((it != 'Y') & (it != 'N')):
                print("Please type only Y or N!")
                TypeError
            if (it == 'Y'):
                print("Continuing plotting...")
                print(f"Current mag cut: {m_lcut:.2f}, {m_hcut:.2f}")
                print(f"Current C cut: {C_lcut:.2f}, {C_hcut:.2f}")

                m_lcut, m_hcut = input("Type new mag range (low mag cut, high mag cut) : ").split(',')
                C_lcut, C_hcut = input("Type new C index range (low C cut, high C cut) : ").split(',')
                m_lcut, m_hcut = float(m_lcut), float(m_hcut)
                C_lcut, C_hcut = float(C_lcut), float(C_hcut)
                plt.savefig(fname+'-check1.png', dpi=300)
                plt.close()

        fig = plt.figure(n_plt, figsize=(13,6))
        gs = GridSpec(1, 2, left=0.08, bottom=0.15, right=0.96, top=0.95,
                      width_ratios=[1., 1.], wspace=0.20)

        # ----- Axis 1 ----- #
        ax = fig.add_subplot(gs[0,0])
        ax.set_xticks(ic.xtic)
        ax.set_yticks([0.0,0.5,1.0,1.5,2.0])
        ax.tick_params(axis='both', labelsize=17.5)
        ax.set_xlabel(ic.maglab[0]+' [mag]',fontsize=17.5)
        ax.set_ylabel('Magnitude error', fontsize=17.5)
        ax.set_xlim(ic.xran)
        ax.set_ylim([0.0,1.0])
        ax.tick_params(width=1.5, length=8.0)
        ax.xaxis.set_minor_locator(ticker.AutoMinorLocator(n=4))
        ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(n=5))
        ax.tick_params(width=1.5,length=5.0,which='minor')
        for axis in ['top','bottom','left','right']:
            ax.spines[axis].set_linewidth(1.5)
        # ------------------ #
        ax.plot(mag[val]+ic.magfac, merr[val], 
                '.', ms=3.0, color='gray', alpha=0.8)

        # ----- Axis 2 ----- #
        ax = fig.add_subplot(gs[0,1])
        ax.set_xticks(ic.xtic)
        ax.set_yticks([0.0,0.5,1.0,1.5,2.0,2.5])
        ax.tick_params(axis='both', labelsize=17.5)
        ax.set_xlabel(ic.maglab[0]+' [mag]',fontsize=17.5)
        ax.set_ylabel('C index', fontsize=17.5)
        ax.set_xlim(ic.xran)
        ax.set_ylim([0.0,2.5])
        ax.tick_params(width=1.5, length=8.0)
        ax.xaxis.set_minor_locator(ticker.AutoMinorLocator(n=4))
        ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(n=5))
        ax.tick_params(width=1.5,length=5.0,which='minor')
        for axis in ['top','bottom','left','right']:
            ax.spines[axis].set_linewidth(1.5)
        # ------------------ #
        ax.plot(mag[val]+ic.magfac, Ci[val],
                '.', ms=3.0, color='gray', alpha=0.7)

        psf1 = (val & (mag+ic.magfac > m_lcut) & (mag+ic.magfac < m_hcut) & \
                (Ci > C_lcut) & (Ci < C_hcut))

        ax.plot(mag[psf1]+ic.magfac, Ci[psf1],
                'o', ms=3.0, color='red', alpha=0.8)
        plt.show(block=False)
        n_plt += 1

        if (ic.plt_interact == False):
            print("Finishing plotting...")
            plt.savefig(fname+'-check1.png', dpi=300)
            plt.close()
            break        

    print(f"Total # of plot iterations : {n_plt:d}")


    # ----- Writing *.reg and *.coo files ----- #

    # Writing *.reg file
    f = open(fname+'_psf.reg','w')
    for i in np.arange(np.sum(psf1)):
        f.write(f"{df_ap['x'][psf1].values[i]:.2f}  {df_ap['y'][psf1].values[i]:.2f}\n")
    f.close()

    # Writing *.lst file
    g = open(cooname,'r')
    line1 = g.readline()
    line2 = g.readline()
    line2 = line2.replace("  1  ", "  3  ", 1)

    f = open(lstname,'w')
    f.write(line1)
    f.write(line2)
    f.write('\n')
    for i in np.arange(np.sum(psf1)):
        f.write(f" {int(df_ap['id'][psf1].values[i]):7d}  {df_ap['x'][psf1].values[i]:8.2f}  {df_ap['y'][psf1].values[i]:8.2f}  {df_ap['mag4'][psf1].values[i]:6.3f}  {df_ap['merr4'][psf1].values[i]:6.3f}\n")
    f.close()
    g.close()



    # ----- Running the 2nd DAOPHOT task w/ PSF info ----- #
    scr2name = 'daophot2.scr'

    os.system('rm -rfv '+neiname+' '+psfname)
    print("\n")
    print("Starting the process for "+fname)
    print("\n")

    run_daophot(ic.nfits[j], scr2name, find=False, phot=False,
                psf=True, psf_ap=False)

    # Iterations
    n_iter = 1
    dat_nei = pd.read_fwf(neiname, dtype=None, header=None, skiprows=3)

    while (len(dat_nei.columns) == 6):

        # Subtracting conditions
        subtract = ((dat_nei[5] == '?') | (dat_nei[5] == '*'))
        id_subtract = dat_nei.loc[subtract, 0].values

        dat_lst = pd.read_fwf(lstname, dtype=None, header=None, skiprows=3)
        
        # Making *.lst file
        g = open(cooname,'r')
        line1 = g.readline()
        line2 = g.readline()
        line2 = line2.replace("  1  ", "  3  ", 1)
       
        f = open(lstname, 'w')
        f.write(line1)
        f.write(line2)
        f.write('\n')
        for i in np.arange(len(dat_lst)):
            if (dat_lst[0].values[i] in id_subtract):
                continue
            else:
                f.write(f" {dat_lst[0].values[i]:7d}  {dat_lst[1].values[i]:8.2f}  {dat_lst[2].values[i]:8.2f}  {dat_lst[3].values[i]:6.3f}  {dat_lst[4].values[i]:6.3f}\n")
        f.close()

        # Running DAOPHOT again
        os.system('rm -rfv '+neiname+' '+psfname)
        os.system('daophot < '+scr2name)
        dat_nei = pd.read_fwf(neiname, dtype=None, header=None, skiprows=3)
        n_iter += 1

    print(f"Total # of PSF iterations : {n_iter:d}")


# Printing the running time
print("--- {0:.1f} seconds ---".format(time.time() - start_time))






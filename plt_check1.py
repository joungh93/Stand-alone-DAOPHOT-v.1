#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 14:32:42 2019

@author: jlee
"""


import time
start_time = time.time()

import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import pandas as pd
import os

import init_cfg as ic


# Magnitude factors
magfac = 2.0 + 2.5*np.log10(ic.ifac)


# Reading data from *.coo file
for j in np.arange(len(ic.nfits)):
    fname = ic.nfits[j].split('.fits')[0]
    apname = fname+'.ap'
    cooname = fname+'.coo'

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

    print("\n")
    print("Starting to plot for "+ic.maglab[j])
    print("\n")
    
    n_plt = 0
    while True:
        it = input("Do you want to plot? (Y/N) : ")
        if (it == 'N'):
            print("Finishing plotting...")
            break
        if ((it != 'Y') & (it != 'N')):
            print("Please type only Y or N!")
            TypeError
        if (it == 'Y'):
            print("Continuing plotting...")
            n_plt += 1

            m_lcut, m_hcut = input("Set the magnitude range (m_lcut, m_hcut) : ").split(',')
            C_lcut, C_hcut = input("Set the C index range (C_lcut, C_hcut) : ").split(',')
            m_lcut, m_hcut = float(m_lcut), float(m_hcut)
            C_lcut, C_hcut = float(C_lcut), float(C_hcut)

            # ----- Figure 1 ----- #
            fig1 = plt.figure(100*j+n_plt, figsize=(13,6))
            ax1 = plt.subplot(1,2,1)
            ax1.set_position([0.08,0.15,0.39,0.80])
            ax1.set_xticks(ic.xtic)
            ax1.set_yticks([0.0,0.5,1.0,1.5,2.0])
            plt.xlabel(ic.maglab[j]+' [mag]',fontsize=17.5)
            plt.ylabel('Magnitude error',fontsize=17.5)
            plt.xlim(ic.xran) ; plt.xticks(fontsize=17.5)
            plt.ylim([0.0,1.0]) ; plt.yticks(fontsize=17.5)
            plt.tick_params(width=1.5, length=8.0)
            plt.minorticks_on()
            plt.tick_params(width=1.5,length=5.0,which='minor')
            for axis in ['top','bottom','left','right']:
                ax1.spines[axis].set_linewidth(1.5)
            # -------------------- #
            plt.plot(mag[val]+magfac, merr[val], 
                    '.', ms=3.0, color='gray', alpha=0.8)

            # ----- Figure 2 ----- #
            ax1 = plt.subplot(1,2,2)
            ax1.set_position([0.57,0.15,0.39,0.80])
            ax1.set_xticks(ic.xtic)
            ax1.set_yticks([0.0,0.5,1.0,1.5,2.0])
            plt.xlabel(ic.maglab[j]+' [mag]',fontsize=17.5)
            plt.ylabel('C index',fontsize=17.5)
            plt.xlim(ic.xran) ; plt.xticks(fontsize=17.5)
            plt.ylim([0.0,2.2]) ; plt.yticks(fontsize=17.5)
            plt.tick_params(width=1.5, length=8.0)
            plt.minorticks_on()
            plt.tick_params(width=1.5,length=5.0,which='minor')
            for axis in ['top','bottom','left','right']:
                ax1.spines[axis].set_linewidth(1.5)
            # -------------------- #    
            plt.plot(mag[val]+magfac, Ci[val],
                    '.', ms=3.0, color='gray', alpha=0.7)

            psf1 = (val & (mag+magfac > m_lcut) & (mag+magfac < m_hcut) & \
                    (Ci > C_lcut) & (Ci < C_hcut))

            plt.plot(mag[psf1]+magfac, Ci[psf1],
                    'o', ms=3.25, color='red', alpha=0.8)
            
            plt.savefig(fname+'-check1.png')


    print("Total # of iterations : {0:d}".format(n_plt))


    # Making region files 
    f = open(fname+'_psf.reg','w')
    # f.write('# Region file format: DS9 version 4.1'+'\n')
    # f.write('global color=red dashlist=8 3 width=2 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1'+'\n')
    # f.write('image'+'\n')
    # for i in np.arange(np.sum(psf1)):
    #     f.write('circle({0:.2f}, {1:.2f}, {2:.2f})'.format(df_ap['x'][psf1].values[i], df_ap['y'][psf1].values[i], 30.0)+'\n')
    # f.close()
    
    for i in np.arange(np.sum(psf1)):
        f.write('{0:.2f}  {1:.2f}'.format(df_ap['x'][psf1].values[i], df_ap['y'][psf1].values[i])+'\n')
    f.close()


    # Making *.lst file
    g = open(cooname,'r')
    line1 = g.readline()
    line2 = g.readline()
    line2 = line2.replace("  1  ", "  3  ", 1)

    f = open(fname+'.lst','w')
    f.write(line1)
    f.write(line2)
    f.write('\n')
    for i in np.arange(np.sum(psf1)):
        f.write(' {0:7d}  {1:8.2f}  {2:8.2f}  {3:6.3f}  {4:6.3f}'.format(int(df_ap['id'][psf1].values[i]), df_ap['x'][psf1].values[i], df_ap['y'][psf1].values[i], df_ap['mag4'][psf1].values[i], df_ap['merr4'][psf1].values[i])+'\n')
    f.close()


# Printing the running time
print("--- {0:.1f} seconds ---".format(time.time() - start_time))

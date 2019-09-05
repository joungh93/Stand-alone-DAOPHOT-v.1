#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 2 17:02:27 2019

@author: jlee
"""


import time
start_time = time.time()


import alipy
import glob, os

import init_cfg as ic


os.system('rm -rfv '+ic.diO)

images_to_align = sorted(glob.glob(ic.diI+"*.fits"))
ref_image = ic.diI+ic.ali_ref

identifications = alipy.ident.run(ref_image, images_to_align, visu=False)
# That's it !
# Put visu=True to get visualizations in form of png files (nice but much slower)
# On multi-extension data, you will want to specify the hdu (see API doc).

# The output is a list of Identification objects, which contain the transforms :
for id in identifications: # list of the same length as images_to_align.
        if id.ok == True: # i.e., if it worked

                print("{0:20s} : flux ratio {1:.2f}".format(id.ukn.name, id.medfluxratio))
                print(id.trans.v)
                print(id.trans.matrixform)
                print(id.trans.inverse())
                # id.trans is a alipy.star.SimpleTransform object. Instead of printing it out as a string,
                # you can directly access its parameters :
                #print id.trans.v # the raw data, [r*cos(theta)  r*sin(theta)  r*shift_x  r*shift_y]
                #print id.trans.matrixform()
                #print id.trans.inverse() # this returns a new SimpleTransform object

        else:
                print("{0:20s} : no transformation found !".format(id.ukn.name))

# Minimal example of how to align images :

outputshape = alipy.align.shape(ref_image)
# This is simply a tuple (width, height)... you could specify any other shape.

for id in identifications:
        if id.ok == True:
                # Using geomap/gregister, correcting also for distortions :
                alipy.align.irafalign(id.ukn.filepath, id.uknmatchstars, id.refmatchstars, shape=outputshape, makepng=False)
                # id.uknmatchstars and id.refmatchstars are simply lists of corresponding Star objects.

                # By default, the aligned images are written into a directory "alipy_out".


# Printing the running time
print("--- {0:.1f} seconds ---".format(time.time() - start_time))
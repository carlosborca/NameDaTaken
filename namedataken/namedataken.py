#!/usr/bin/env python

#
# @BEGIN LICENSE
#
# NameDaTaken: Rename your photos based on the date they were taken.
#
# Copyright (c) 2020 
# Carlos H. Borca
#
# The copyrights for code used from other parties are included in
# the corresponding files.
#
# This file is part of NameDaTaken.
#
# NameDaTaken is free software; you can redistribute it and/or modify
# it under the tesms of the GNU Lesser General Public License as 
# published by the Free Software Foundation, version 3.
#
# NameDaTaken is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public 
# License along with NameDaTaken; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 
# 02110-1301 USA.
#
# @END LICENSE
#

#NOTE: conda create -n NDT python=3.8 exifread -c conda-forge

# Import standard Python modules.
import os
import sys
import exifread # Get from: conda install -c conda-forge exifread 

d = os.getcwd()

for fn in os.listdir(d):
    
    # TODO: Check an alternative for different extensions at:
    # https://stackoverflow.com/questions/45637600/using-endswith-with-case-insensivity-in-python
    if fn.lower().endswith('.jpg'):

        pfn = os.path.join(d, fn)

        print("Filepath: {}".format(pfn)) #debug

        #newfn = getNewFileName(pfn)

        with open(pfn, 'rb') as pf:
            
            exif = exifread.process_file(pf) # Get EXIF data from file.

            #[print(i, exif[i]) for i in exif if "Date" in i] #debug

            try:
                dt = str(exif['EXIF DateTimeOriginal']) # Try to get original date and time.

            except KeyError:

                try:
                    dt = str(exif['EXIF DateTimeDigitized']) # Else, try to get digitized date and time.
                
                except KeyError:

                    try:
                        dt = str(exif['Image DateTime']) # Finally, try to get the image date and time, else quit.
                    
                    except:
                        print("\nERROR: Cannot extract date and time.\n")
                        sys.exit()

            #print(dt) #debug

            dtd, dtt = dt.split(" ", 1) # Split into date and time.
            #print(dtd, dtt) #debug

            day  = dtd.replace(":", "-")
            time = dtt.replace(":", ".")
            #print(day, time) #debug

            newfn = "{} {}.JPG".format(day, time)
            print(newfn) #debug


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


# ======================================================================================================================
def getDateTime(original):
    """Gets the date and time from the EXIF information of the file and returns them on a format designed to math that 
    of Dropbox: YYYY-MM-DD HH.MM.SS

    Arguments:
    <str> original
        Path and name of a file.

    Returns:
    <str> date
        YYYY-MM-DD
    <str> time
        HH.MM.SS
    """
 
    with open(original, "rb") as f:

        exif = exifread.process_file(f) # Get EXIF data from file.

        #[print(i, exif[i]) for i in exif if "Date" in i] #debug

        try:
            dt = str(exif["EXIF DateTimeOriginal"]) # Try to get original date and time.
            gdtSuccess = True

        except KeyError:

            try:
                dt = str(exif["EXIF DateTimeDigitized"]) # Else, try to get digitized date and time.
                gdtSuccess = True

            except KeyError:

                try:
                    dt = str(exif["Image DateTime"]) # Finally, try to get the image date and time, else quit.
                    gdtSuccess = True

                except:
                    print("\nWARNING: Cannot extract date and time from file {}\n".format(original))
                    gdtSuccess = False

                    # Return before processing any further.
                    return None, None, gdtSuccess

        #print(dt) #debug

        dtd, dtt = dt.split(" ", 1) # Split into date and time.
        #print(dtd, dtt) #debug

        date = dtd.replace(":", "-")
        time = dtt.replace(":", ".")
        #print(day, time) #debug

        return date, time, gdtSuccess
# ======================================================================================================================


# ======================================================================================================================
def getMotoRazr(fn):
    """Gets the date and time from the name of the file and returns them on a format designed to math that of Dropbox: 
    YYYY-MM-DD HH.MM.SS

    Arguments:
    <str> original
        Path and name of a file.

    Returns:
    <str> date
        YYYY-MM-DD
    <str> time
        HH.MM.SS
    """

    d, t = fn[:-4].split("_", 1) # Split into date and time.
    
    #print("{} {}".format(d, t)) #debug

    date = "20{}-{}-{}".format(d[6:], d[3:5], d[:2])
    time = "{}.{}.00".format(t[:2], t[2:4])

    #print("{} {}".format(date, time)) #debug
    
    return date, time
# ======================================================================================================================


# ======================================================================================================================
def main():

    fCount = 0
    d = os.getcwd()

    # TODO: (1) Check an alternative for different extensions:
    #exts = [".avi", ".jpg", ".mp4", ".mpg", ".png"]
    exts = [".jpg"]

    for fn in os.listdir(d):

        for extension in exts:

            if fn.lower().endswith(extension):

                original = os.path.join(d, fn)

                # Get the date and time of the original file.
                date, time, gdtSuccess = getDateTime(original)

                # If retrieval of date and time was successful, proceed to creating the new file name.
                if gdtSuccess:

                    newfn = "{} {}{}".format(date, time, extension.lower())
                    #print("Old Name: {}".format(fn)) #debug
                    #print("Old: {}".format(original)) #debug

                    if newfn.lower() != fn.lower():
                    
                        new = os.path.join(d, newfn)
                        #print("New Name: {}".format(newfn)) #debug
                        #print("New: {}".format(new)) #debug

                if not gdtSuccess:

                    if ((fn[2] == "-" and fn[5] == "-") and (fn[8] == "_" and len(fn) >= 17)):
                        
                        date, time = getMotoRazr(fn)
                        print("date = {}, time = {}".format(date, time)) #debug
                    
                        newfn = "{} {}{}".format(date, time, extension.lower())
                        #print("Old Name: {}".format(fn)) #debug
                        #print("Old: {}".format(original)) #debug

                        if newfn.lower() != fn.lower():
                    
                            new = os.path.join(d, newfn)
                            #print("New Name: {}".format(newfn)) #debug
                            #print("New: {}".format(new)) #debug

                    else:
                        print("\nWARNING: Cannot extract date and time from file {}\n".format(original))
                    
                if ("new" in locals() and date != None):                    

                    # Need a safe method to rename files. While the new file name exists, append a numerical index
                    # until the new file name does not match any existing files, to avoid overwritting.
                    add = 0

                    while os.path.exists(new):

                        add += 1
                        newfn = "{} {}-{}{}".format(date, time, add, extension.lower())
                        new = os.path.join(d, newfn)

                    # Once there is no conflict with the new file name...
                    else:

                        try:

                            # Try rename operation.
                            os.rename(original, new)

                        except PermissionError:

                            # For permission related errors.
                            print("Operation not permitted.")

                        except OSError as error:

                            # For other errors.
                            print(error)

                        # Count the file as renamed.
                        print("Renaming: {} -> {}".format(fn, newfn)) #debug
                        fCount += 1
                
    print("Successfully renamed {} media files.".format(fCount))
# ======================================================================================================================

if __name__ == "__main__":
    main()

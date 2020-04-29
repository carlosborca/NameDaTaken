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
    """Gets the date and time from the EXIF information of the file and
    returns them on a format designed to math that of Dropbox:
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
 
    with open(original, "rb") as f:

        exif = exifread.process_file(f) # Get EXIF data from file.

        #[print(i, exif[i]) for i in exif if "Date" in i] #debug

        try:
            dt = str(exif["EXIF DateTimeOriginal"]) # Try to get original date and time.
            success = True

        except KeyError:

            try:
                dt = str(exif["EXIF DateTimeDigitized"]) # Else, try to get digitized date and time.
                success = True

            except KeyError:

                try:
                    dt = str(exif["Image DateTime"]) # Finally, try to get the image date and time, else quit.
                    success = True

                except:
                    print("\nWARNING: Cannot extract date and time from file {}\n".format(original))
                    success = False

                    # Return before processing any further.
                    return None, None, success

        #print(dt) #debug

        dtd, dtt = dt.split(" ", 1) # Split into date and time.
        #print(dtd, dtt) #debug

        date = dtd.replace(":", "-")
        time = dtt.replace(":", ".")
        #print(day, time) #debug

        return date, time, success
# ======================================================================================================================


# ======================================================================================================================
def main():

    fCount = 0
    d = os.getcwd()

    # TODO: (2) Check an alternative for different extensions at:
    #exts = [".avi", ".jpg", ".mp4", ".mpg", ".png"]
    exts = [".jpg"]

    for fn in os.listdir(d):

        for extension in exts:

            if fn.lower().endswith(extension):

                original = os.path.join(d, fn)

                # Get the date and time of the original file.
                date, time, success = getDateTime(original)

                # If retrieval of date and time was successful, proceed to creating the new file name.
                if success:

                    fCount += 1
                    #print("Old: {}".format(original)) #debug

                    newfn = "{} {}{}".format(date, time, extension.upper())
                    #print("New Name: {}".format(newfn)) #debug

                    new = os.path.join(d, newfn)
                    #print("New: {}".format(new)) #debug

                    # Need a safe method to rename files. While the new file name exists, append a numerical index until the
                    # new file name does not match any existing files, to avoid overwritting.

                    add = 0

                    while os.path.exists(new):

                        add += 1
                        new = "{} {}-{}{}".format(date, time, add, extension.upper())

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

    print("Successfully renamed {} media files.".format(fCount))
# ======================================================================================================================

if __name__ == "__main__":
    main()

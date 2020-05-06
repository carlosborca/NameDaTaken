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


# ======================================================================================================================
def main():

    fCount = 0
    d = os.getcwd()

    # TODO: (1) Check an alternative for different extensions:
    #exts = [".AVI", ".JPG", ".MP4", ".MPG", ".PNG"]
    exts = [".JPG"]

    for fn in os.listdir(d):

        for extension in exts:

            if fn.endswith(extension):

                fnlow = fn[:-4] + fn[-4:].lower()

                original = os.path.join(d, fn)
                new      = os.path.join(d, fnlow)
                    
                # Need a safe method to rename files. While the new file name exists, append a numerical index
                # until the new file name does not match any existing files, to avoid overwritting.
                add = 0
                
                while os.path.exists(new):

                    add += 1
                    newfn = "{}-{}{}".format(fn[:-4], add, fn[-4:].lower())
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
                    print("Renaming: {} -> {}".format(original, new)) #debug
                    fCount += 1
                
    print("Successfully renamed {} media files.".format(fCount))
# ======================================================================================================================

if __name__ == "__main__":
    main()

#!/usr/bin/env python

#
# @BEGIN LICENSE
#
# NameDaTaken: Rename your photos based on the date they were taken.
#
# Copyright (c) 2023
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

#NOTE: conda create -n NDT python=3.8 exifread mutagen -c conda-forge

import os
import re
from mutagen.easyid3 import EasyID3

# ======================================================================================================================
def sanitize_filename(filename):
    # Replace problematic characters except apostrophes with underscores
    sanitized = re.sub(r'[\/:*?"<>|]', '_', filename)
    return sanitized.replace("'", "’")  # Replace single quote with apostrophe
# ======================================================================================================================

# ======================================================================================================================
def rename_mp3_files(directory):
    
    fCount = 0 

    for filename in os.listdir(directory):

        if filename.endswith('.mp3'):
            filepath = os.path.join(directory, filename)
            audiofile = EasyID3(filepath)

            if 'artist' in audiofile and 'title' in audiofile:  
                artists = audiofile['artist']
                title = audiofile['title'][0]
                
                if artists and title:
                    first_artist = artists[0]
                    sanitized_artist = sanitize_filename(first_artist)
                    sanitized_title = sanitize_filename(title)
                    new_filename = f"{sanitized_artist} - {sanitized_title}.mp3"
                    new_filepath = os.path.join(directory, new_filename)

                    if not os.path.exists(new_filepath):
                        os.rename(filepath, new_filepath)
                        print(f"Renamed '{filename}' to '{new_filename}'")
                        fCount += 1

                    else:
                        print(f"File '{new_filename}' already exists. Skipped.")
                else:
                    print(f"File '{filename}' does not have complete artist and title tags. Skipped.")
            else:
                print(f"File '{filename}' does not have ID3 tags. Skipped.")

    return fCount
# ======================================================================================================================

# ======================================================================================================================
def main():

    current_directory = os.getcwd()
    fCount = rename_mp3_files(current_directory)

    print("Successfully renamed {} media files.".format(fCount))

    return 0
# ======================================================================================================================

if __name__ == "__main__":
    main()

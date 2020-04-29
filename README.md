# NameDaTaken

Automated renaming of media files according to their creation date and time.

| Category | Badges |
|-------------|-------------|
| **Foundation** | [![License](https://img.shields.io/github/license/carlosborca/NameDaTaken.svg)](https://opensource.org/licenses/LGPL-3.0) [![GitHub Top Languages](https://img.shields.io/github/languages/top/carlosborca/NameDaTaken)](https://github.com/carlosborca/NameDaTaken/) |
| **GitHub Info** | [![GitHub Code Size](https://img.shields.io/github/languages/code-size/carlosborca/NameDaTaken)](https://github.com/carlosborca/NameDaTaken/) [![GitHub Commits per Month](https://img.shields.io/github/commit-activity/m/carlosborca/NameDaTaken)](https://github.com/carlosborca/NameDaTaken/) [![GitHub Last Commit](https://img.shields.io/github/last-commit/carlosborca/NameDaTaken)](https://github.com/carlosborca/NameDaTaken/) |

## Overview

NameDaTaken is a Python 3 code that automates renaming of media files according their creation date and time following the format 'YYYY-MM-DD HH.MM.SS.ext', commonly used by Dropbox.

## General Information

To run NameDaTaken, the code requires Python 3 and its `exifread` module. So, the instructions to download and install NameDaTaken and to create a _conda environment_ that includes exifread are presented below.

### Installation

Minimal set of commands to install NameDaTaken on Linux, MacOS, or Windows (with the Windows Subsystem for Linux). Last tested on 29 April 2020:

#### 1. Install Miniconda:

If you have an installation of _Conda_ in your system, please skip to step 2. Otherwise, _Miniconda_ is required and the installer is available from the the Anaconda website. To download the installer from the terminal (in Linux or the Windows Subsystem for Linux):

```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

(_Note_) If you use MacOS, replace `Linux` by `MacOSX` on the previous command.

Run the installer following the on-screen instructions:

```
bash Miniconda3-latest-Linux-x86_64.sh
```

After the installation is complete, close the terminal and start a new shell.

(_Optional_) Disable automatic activation of the _base_ conda environment:

```
conda config --set auto_activate_base false
```

#### 2. Create a _Conda Environment_ for NameDaTaken

NameDaTaken requires Python 3 and a module to extract the EXIF data out of media files. Conda offers the possibility of creating an _environment_ that contains all the dependencies required by NameDaTaken. To download and install the required software tools in a new _NDT_ environment execute the command below and follow the on-screen instructions:

```
conda create -n NDT python=3.8 exifread -c conda-forge
```

#### 3. Activate the _NDT_ environment

To use the recently created _NDT_ environment, activate it:

```
conda activate NDT
```

#### 4. Clone NameDaTaken from its GitHub repository:

In you file system navigate to the location where you would like to place the root directory of NameDaTaken and clone it from its corresponding GitHub repository:

```
git clone https://github.com/carlosborca/NameDaTaken.git

### How to run NameDaTaken

The code uses the _current working directory_ as a reference point for execution and it will rename all the files that match the supported media extensions on that directory. Therefore, one needs to navigate to the folder where the media files are located and execute the Python 3 code there.

#### Copyright

Copyright (c) 2020, Carlos H. Borca

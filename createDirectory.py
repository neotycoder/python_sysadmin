#!/usr/bin/python

# Author: Ty Lim
# Date: 2/4/2015
# File name: createDirectory.py
# Description: This is a simple example of how to check to see if a directory exist, and if not, create it.
# This script also shows an example of how to create a file name with a time stamp, use that filen name
# to open a file for writing, and write to the file, and finally, close it.

# This is nothing too difficult, and you can certainly add more functionality to it if you wish.
# One idea is to build this whole example into an object with subsequent methods.

import os, datetime

# Create the file name
baseFileName = "12345"
app="someAppName"
dateTimeStamp = datetime.date.today()
# This directory needs to exists. It is the parent directory that will house the datafiles.
targetDirectory = "/tmp/datafiles"
targetfileName = str(baseFileName)+"_"+app+"."+str(dateTimeStamp)+".txt"
fullPathToFile = targetDirectory+"/"+targetfileName

print("FileName: " + fullPathToFile)

# Check base path. If it does not exist, create it.
if not os.path.isdir(targetDirectory):
    os.makedirs(targetDirectory)

file = open(fullPathToFile,'w')
file.write("This is a test.")


file.close()



    






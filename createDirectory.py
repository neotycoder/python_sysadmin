#!/usr/bin/python

# Author: Ty Lim
# Date: 2/4/2015
# File name: createDirectory.py
# Python Version: 3.X
# Description: This script shows the example of how concatenation works in python, utilizing the os module to check a directory
# and create it if it does not exist, and opening and closing a file for writing.
# 
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



    






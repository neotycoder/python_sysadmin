#!/usr/bin/python3

"""
	Name: systemGather.py
	Author: Ty Lim
	Date: July 14, 2016
	Description: Simple example on how to use the subprocess module to gather some system info.

	Usage:

		> ./systemGather.py

"""
import subprocess


def uname_func():
	command = "uname"
	command_arg = "-a"
	print ("System Gathering info with %s command:\n" % command)
	subprocess.call([command, command_arg])

def diskspace_func():
	diskspace = "df"
	diskspace_arg = "-k"
	print ("Disk Space info gathering using %s command:\n" % diskspace)
	subprocess.call([diskspace, diskspace_arg])

def main():
	# Getting 'uname' info
	uname_func()

	# Getting 'diskspace' info
	diskspace_func()


if __name__ == '__main__':
	main()
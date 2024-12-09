#!/usr/bin/python3

import os

# get current working directory
print(f'os.getcwd() = {os.getcwd()}')

# change directory
os.chdir('/tmp')

# list files and directories (including hidden)
print(os.listdir())

# Iterate over files using `name` attribute 
print([dir.name for dir in os.scandir('/tmp')])

#!/usr/bin/python


import glob


for file in glob.glob('./*_sample_dir'):
    print(file)
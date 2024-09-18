#!/usr/bin python3

import glob
#import os
#import hashlib
#from PIL import Image

for file in sorted(glob.glob('./*_sample_dir/**')):
    print(file)

'''
goal is make a tar script that will first hash
image/doc add that hash to a db, compress with xz
either on file or folder level to send to a cloud 
backup 
'''

# first take hashes of a dir of files and print
# https://builtin.com/data-science/python-list-files-in-directory

#def dir_to_list():

#files = os.listdir("./sample_dir/")

#a=os.scandir()
'''
    for x in range(len(l)):
        print (a[x])
'''
'''
#md5 - hashlib.md5()

#with open(sys.argv[1], 'rb') as f:
 #   while True:
# BUF_SIZE = 65536 
# reads in 64kb chunks if ram is limited


# md5 is being used for speed and security is unecessary
# for the purpose it is serving

def sha256sum(filename)
    with open(filename, )

print(exfile)
'''
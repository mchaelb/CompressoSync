#!/usr/bin/env python3

import os
import hashlib

def transform_hash (direc):
    for root,dirs,files in os.walk(direc):
        for file in files:
            print(os.path.join(root, file))
'''
def makehash(baseDir):
    for entry in os.scandir(baseDir):
        if entry.is_file():
            yield os.path.join(baseDir, entry.name)
        else:
            yield scanRecurse(entry.path)
  
for i in makehash('./a_sample_dir'):
    print(i)
#from PIL import Image
'''
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
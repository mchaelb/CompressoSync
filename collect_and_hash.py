#!/usr/bin python3

import glob
import hashlib

# from PIL import Image

# FIRST option reads in 64kb chunks if ram is limited
# NOTE: md5 is for unique ID and speed, not security

collection_dict = {}
BUF_SIZE = 65536

for file in sorted(glob.glob('./*_sample_dir/**')):
    md5 = hashlib.md5()
    with open(file, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
    file_hash = md5.hexdigest()
    # Add the file path as the key and the MD5 hash as the value
    collection_dict.update({file: file_hash})
    # add file path and hash to dictionary object
    
# print(collection_dict)
# verify dictionary object created correctly

#################################################################

# import os (to use os.walk/scandir)
# https://builtin.com/data-science/python-list-files-in-directory

'''
glob function grabs a list of files within a directory based on 
a regex pattern of directories/subdirectories, via pattern matching. 
therefore, glob is best for known file paths/directories, where 
os.walk would be better for unknown recursive directory paths, 
finding each subdir in a dir tree. os.walk is better for tracking 
paths in a more complex and dynamic filesystem both for archiving
and documentation for dir/subdir/filename organization. os.walk is not 
ideal for the end state of this application, which is to efficiently 
compress, diff, and then push (if needed) backups. note that glob only 
takes 1 positional argument, so file naming convention will have to 
fit into pattern established by /path/to/dir/**/* python 3.5
supports **/*, which is a recursive wildcard pattern. 
'''

#################################################################

# SECOND option glob alone to get a list of files

# for file in sorted(glob.glob('./*_sample_dir/**')):
#     print(file)

#################################################################

# THIRD option to list files, hash, and add to dictionary
# collection_dict = {}

# for file in sorted(glob.glob('./*_sample_dir/**')):
#     with open(file, 'rb') as f:
#         file_hash = hashlib.md5(f.read()).hexdigest()
#     # this adds file path and hash to dictionary object
#     collection_dict[file] = file_hash
#     # this prints filedirectory_hash in a string to verify
# print(collection_dict) 

#################################################################


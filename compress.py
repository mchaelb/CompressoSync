#!/usr/bin python3

import glob
import hashlib
# import os (to use os.walk/scandir)
# https://builtin.com/data-science/python-list-files-in-directory
# from PIL import Image

'''
glob function grabs a list of files within a directory based on 
a regex pattern of directories/subdirectories. i.e. is not directory
traversal per se, but pattern matching. therefore, glob is best for
known file paths/directories, where as os.walk would be better for
unknown recursive directories, finding each subdir in a dir tree.
os.walk may be better for tracking absolute paths in a more complex 
and dynamic filesystem both for archiving (backups will be complete),
and a visual reminder of actual dir/subdir/filename organization.
for speed, os.walk is not ideal for the end state of this application,
which is to efficiently compress, diff, and then push (if needed) backups.
note that glob only takes 1 positional argument, so file naming convention
will have to fit into pattern established by /path/to/dir/**/* python 3.5
supports **/*, which is a recursive wildcard pattern. 
'''

# FIRST option glob alone to get a list of files
# for file in sorted(glob.glob('./*_sample_dir/**')):
#     print(file)

'''
goal is make a tar script that will first hash
image/doc add that hash to a db, compress with xz
either on file or folder level to send to a cloud 
backup 
'''

# SECOND option to list files and hash them
# for file in sorted(glob.glob('./*_sample_dir/**')):
#     with open(file, 'rb') as f:
#         file_hash = hashlib.md5(f.read()).hexdigest()
#     print(f"File: {file}, MD5 Hash: {file_hash}")

# BUF_SIZE = 65536 
# reads in 64kb chunks if ram is limited

BUF_SIZE = 65536  # reads in 64kb chunks

for file in sorted(glob.glob('./*_sample_dir/**')):
    md5 = hashlib.md5()
    with open(file, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
    file_hash = md5.hexdigest()
    print(f"File: {file}, MD5 Hash: {file_hash}")

# md5 is being used for speed and security is unecessary
# for the purpose it is serving
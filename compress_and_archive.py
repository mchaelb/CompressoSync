#!/usr/bin python3

from collect_and_hash import collection_dict
import pickle
import tarfile
import io

# print(collection_dict)

serial_dict = pickle.dumps(collection_dict)
with tarfile.TarFile('output.tar', 'w') as tar:
    bytes_io = io.BytesIO(serial_dict)
    # add the serialized dictionary to the tarfile
    tarinfo = tarfile.TarInfo('serial_dict.pkl')
    
    tarinfo.size = len(serial_dict)
    tar.addfile(tarinfo, fileobj=bytes_io)



# 1. Extract the serialized dictionary from the tarfile
with tarfile.TarFile('output.tar', 'r') as tar:
    serial_dict = tar.extractfile('serial_dict.pkl').read()

# 2. Deserialize the dictionary
new_collection_dict = pickle.loads(serial_dict)

# 3. Print the deserialized dictionary
print(new_collection_dict)  


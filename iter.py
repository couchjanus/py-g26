list = [1,2,3,4,5]

# for i in list:
#     print(i)

itr = iter(list)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))


import os, hashlib


def walk(dir):
    files = {}
    for file in [item for item in os.listdir(dir) if os.path.isfile(os.path.join(dir, item))]:
        hash = hashlib.md5()
        with open(os.path.join(dir, file), encoding='utf-8') as f:
            for chunk in iter(lambda: f.read(2048),""):
                hash.update(chunk.encode('utf-8'))
        md5 = hash.hexdigest()
        files[file] = md5
    return files
       
files = walk(os.getcwd())


FILEBAME = 'repohash'

import shelve

for k,v in files.items():
    with shelve.open(FILEBAME) as repo:
        repo[k] = v

with shelve.open(FILEBAME) as repo:
    for f in repo.keys():
        print(f)
        
    for f in repo.values():
        print(f)
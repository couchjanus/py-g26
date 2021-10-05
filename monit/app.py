import os
import sys

# print(len(sys.argv))

help = '''
    Use: {} --name <dir name>
    or:  {} -n <dir name>
'''

if len(sys.argv) == 1:
    print('Too few params')
    print(help.format(sys.argv[0], sys.argv[0]))
    sys.exit(1)

name = sys.argv[1]

if name == '--name' or name == '-n':
    value = sys.argv[2] if len(sys.argv) == 3 else '.'
    print(value)
else:
    print('Error, Unknown param {}'.format(name))
    print(help.format(sys.argv[0], sys.argv[0]))
    sys.exit(1)
    
files = []
dirs = []
d = {}

for dirname, dirnames, filenames in os.walk(value):
    for dir in dirnames:
        d = {
            'path': os.path.join(dirname, dir),
            'recursive': True
        }
        dirs.append(d)
        
    for file in filenames:
        d = {
            'path': os.path.join(dirname, file),
        }
        files.append(d)

print(files)
print(dirs)
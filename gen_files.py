#!python
from os import mkdir, sep
from sys import argv

MBSize = 1024*1024

try:
    fsize = int(argv[1])
    nfiles = int(argv[2])

    dirname = f'{fsize}MB-{nfiles}F'
    mkdir(dirname)

except(IndexError):
    print('USE: python gen_files.py [fsize] [nfiles]')

except(FileExistsError):
    print(f'DIR: {dirname} arredy exist.')

else:
    for n in range(nfiles):
        with open(f'{dirname}{sep}{n}.bin', 'wb') as file:
            for _byte in range(MBSize*fsize):
                file.write(b'0');

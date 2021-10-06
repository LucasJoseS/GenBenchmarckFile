#!python
from os import mkdir, sep
from sys import argv

def main(fsize, n):
    dirname = f"{fsize}-{n}"
    try:
        mkdir(dirname)
    except:
        print(f"dir {dirname} arredy exists.")

    for n in range(n):
        with open(f"{dirname}{sep}{n+1}.bin", "wb") as file:
            for c in range(1024*1024*fsize):
                file.write(b'0');


if(__name__ == "__main__"):
    try:
        fsize = int(argv[1])
        n = int(argv[2])
    except:
        print("python gen_files.py [fsize] [n]")
    else:
        main(fsize, n)

#!python
from os import mkdir, sep

def main(fsize, n):
    mkdir(f"{fsize}-{n}")
    for n in range(n):
        with open(f"{fsize}{sep}{n+1}.bin", "wb") as file:
            for c in range(1024*1024*filesize):
                file.write(b'0');


if(__name__ == "__main__"):
    main(10, 50);
    main(50, 10);
    main(100, 5);
    main(500, 1);
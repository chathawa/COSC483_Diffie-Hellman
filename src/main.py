"""Driver code for Diffie-Hellman
COSC483 -- Applied Crypto -- with Dr. Ruoti
@author: Clark Hathaway
"""

from primes import strong
from math import log2, floor
from time import time
from sys import argv


def main():
    start = time()
    p = strong(debug_int=1000 if len(argv) < 2 else int(argv[1]))
    end = time()

    print('\n'.join((
        f"p = {p}",
        f"bits = {floor(log2(p)) + 1}",
        f"elapsed time = {end - start} sec"
    )))


if __name__ == '__main__':
    main()

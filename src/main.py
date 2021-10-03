"""Driver code for Diffie-Hellman
COSC483 -- Applied Crypto -- with Dr. Ruoti
@author: Clark Hathaway
"""

from primes import strong
from math import log2, floor
from time import time


def main():
    start = time()
    p = strong()
    end = time()

    print('\n'.join((
        f"p = {p}",
        f"bits = {floor(log2(p)) + 1}",
        f"total elapsed time = {end - start} sec"
    )))


if __name__ == '__main__':
    main()

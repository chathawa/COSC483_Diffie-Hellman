"""Strong prime generation.
A prime number p is a strong prime if (p - 1) / 2 is also a prime number.

Additionally, for Diffie-Hellman, p must be at least 1024 bits.
This is accomplished using a random range function with
lower and upper bounds, respectively:
 - the smallest 1024-bit integer, 2^1023, and
 - 2^1032 (arbitrary but this gives a solid range to work with)

Let q = (p - 1) / 2 such that p = 2q + 1.
Since q is also a prime number, it is odd and can be represented as
2k + 1 for some integer k.

The bounds for the random range function can be adjusted so that
we do not generate p and then determine if both it and q are odd numbers,
but generate k and guarantee q = 2k + 1 is odd, as well as 2q + 1.

If a = 2^1023 and b = 2^1032, then a <= p < b.
-> a <= 2q + 1 < b
-> a <= 2(2k + 1) + 1 < b
-> a <= 4k + 3 < b
-> (a - 3) / 4 <= k < (b - 3) / 4
We drop off the -3/4 term because it is less than 1 and just reduce these by 2^-2, getting:
a = 2^1021 and b = 2^1030
"""

from random import randrange
from Crypto.Util.number import isPrime


_LOWER_BOUND, _UPPER_BOUND = (
        2**1021,
        2**1030
)


def strong() -> int:
    q, p = 1, 1

    while not isPrime(p) or not isPrime(q):
        k = randrange(_LOWER_BOUND, _UPPER_BOUND)
        q = 2 * k + 1
        p = 2 * q + 1

    return p

"""Strong prime generation.
A prime number p is a strong prime if (p - 1) / 2 is also a prime number.

Additionally, for Diffie-Hellman, p must be at least 1024 bits.
This is accomplished using a random range function with
lower and upper bounds, respectively:
 - the smallest 1024-bit integer, 2^1023, and
 - 1 + the largest 2048-bit integer, 2^2048 (this bound is exclusive).

Let q = (p - 1) / 2 such that p = 2q + 1.
Since q is also a prime number, it is odd and can be represented as
2k + 1 for some integer k.

The bounds for the random range function can be adjusted so that
we do not generate p and then determine if both it and q are odd numbers,
but generate k and guarantee q = 2k + 1 is odd, as well as 2q + 1.

If a = 2^1023 and b = 2^2048, then a <= p < b.
-> a <= 2q + 1 < b
-> a <= 2(2k + 1) + 1 < b
-> a <= 4k + 3 < b
-> (a - 3) / 4 <= k < (b - 3) / 4
So the new bounds a' and b' are (a - 3) / 4 and (b - 3) / 4, respectively.
"""

from random import randrange
from sys import stderr
from sympy import isprime


_LOWER_BOUND, _UPPER_BOUND = (
        2**1021,
        2**2046
)


def _debug_strong(k, q, p, num_iter):
    stderr.write('\n'.join((
        f"{symbol}={value}" for symbol, value in (
            ("num_iter", num_iter),
            ('k', k),
            ('q', q),
            ('p', p)
        )
    )))


def strong(debug_int=None) -> int:
    k, q, p = None, None, 1
    num_iter = 0

    while not isprime(p):
        num_iter += 1
        k = randrange(_LOWER_BOUND, _UPPER_BOUND)
        q = 2 * k + 1
        p = 2 * q + 1

        if (
            debug_int is not None and
            debug_int > 0 and
            num_iter % debug_int == 0
        ):
            _debug_strong(k, q, p, num_iter)

    if debug_int == -1:
        _debug_strong(k, q, p, num_iter)

    return p
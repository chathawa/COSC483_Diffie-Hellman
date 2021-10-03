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
from time import time
from Crypto.Util.number import isPrime


_LOWER_BOUND, _UPPER_BOUND = (
        2**1023,
        2**2048
)


def strong(debug_int=None) -> int:
    p = 1
    num_iter = 0
    primality = [(False, False)]

    start = time()
    while p % 2 == 0 or False in primality[-1]:
        num_iter += 1

        if debug_int is not None and 0 < num_iter and num_iter % debug_int == 0:
            end = time()
            p_rate, q_rate = 0, 0
            for p_prime, q_prime in primality:
                if p_prime:
                    p_rate += 1
                if q_prime:
                    q_rate += 1

            stderr.write('\n'.join((
                f"Iteration: {num_iter}",
                f"Last {debug_int} iterations elapsed time: {end - start} sec",
                f"Primality rate for p = {100 * p_rate / len(primality):.3f}%",
                f"Primality rate for q = {100 * q_rate / len(primality):.3f}%"
            )) + '\n')
            primality = []
            start = time()
        
        p = randrange(_LOWER_BOUND, _UPPER_BOUND)
        primality.append((
            isPrime(p),
            isPrime((p - 1) // 2)
        ))
    return p


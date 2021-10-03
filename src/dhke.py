"""Diffie-Hellman Key Exchange functions and primitives
"""

from math import floor, log2
from typing import Tuple
from random import randrange


_LOWER_BOUND = 2**6
_UPPER_BOUND = 2**9


def private_keys() -> Tuple[int, int]:
    """Generate two private keys, a & b"""
    a, b = 0, 0

    while a == b:
        a, b = (
            randrange(_LOWER_BOUND, _UPPER_BOUND) for _ in range(2)
        )
    return a, b


def fme(key: int, base: int, p: int) -> int:
    """Fast Modular Exponentiation g^key mod p"""
    key_exp = tuple(
        n for n in range(0, floor(log2(key)) + 1) if key >> n & 1
    )

    g_pow = [base % p]
    for exp in range(1, key_exp[-1] + 1):
        g_pow.append(g_pow[exp - 1]**2 % p)

    result = 1
    for exp in key_exp:
        result *= g_pow[exp]
    return result % p

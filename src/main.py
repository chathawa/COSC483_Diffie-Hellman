"""Driver code for Diffie-Hellman
COSC483 -- Applied Crypto -- with Dr. Ruoti
@author: Clark Hathaway
"""

from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from dhke import private_keys, fme
from primes import strong
from math import log2, floor, ceil
from time import time


def num_bits(n: int) -> int:
    """The bits required to represent n"""
    return floor(log2(n)) + 1


def main():
    start = time()
    p = strong()
    end = time()

    print('\n'.join((
        f"p = {p}",
        f"bits = {num_bits(p)}",
        f"total elapsed time = {end - start} sec"
    )))

    g = 5
    print(f"g = {g}")

    a, _ = private_keys()

    print(f"a = {a}")

    g_a = fme(a, g, p)

    print(f"g^a mod p = {g_a}")

    g_b = 2864220205472957923887303824119489354917231579835996868818203364068334600933983387920047952585445437725015977496806072382480033624893482776888311615535882775116442471144619765035710134159496495517143484426454193100368469802253116761640254710645190448746109640895962505300636991847114900035732583754223824122521
    shared_key = fme(a, g_b, p)

    print(f"g^ab = {shared_key}")

    sha = SHA256.SHA256Hash()
    shared_key = shared_key.to_bytes(ceil(num_bits(shared_key) // 8) + 1, 'big')
    print(f"shared_key (bytes): {shared_key}")
    sha.update(shared_key)
    digest = sha.digest()
    symmetric_key = digest[:16]
    plaintext = AES.new(
        key=symmetric_key,
        mode=AES.MODE_CBC,
        IV=bytes.fromhex('ad8d8ccb5f0ec5b81267244bc886e276')
    ).decrypt(bytes.fromhex('4297d1be983532adc5edde04f0db197ed3aba21348300f7dcf4939622f0199ec7a2b28ecbd80f9a1be1431ccc0277116bb2f36b09ff4481fcbf32d9640705d4eece89821690769f0a566d15ef201bcefa6298dbed21a96df7a7cff61fd8446e57f00abf31a45998842b3ee30195f1c5aae1f11faf7c8ece752f37928171d5d86136d98f72961f7584bfe6bd65779b0338a503a0007e562d32de432112dc8a686a14b763d4b3966ee1c741d0ea96aa327a635a19a558ab739f110e0885e5784ce0c114d8cfb5cd47369f72b40ece596520a97aee2301fe39fbfdb0394fd34e2c3ecaa749c2db61c2ef164f7c05f53ba8945031cbccf2f1f22b070c869a047198c767e2a8d5fe422515a3fed6b4586728d73ab8cc980bd044455c34ca0725bb66554e0daf8136d3f1022b428260c051e4aaae1af27830dbb13affdf6258348252b984230ae9d24d0736f890a617c4986b2f80b5a551a3be80f226717db163fc1ca09b6b98ba708bd89b5b4367182969ddc2f8f8791cf8007d5fc1a8a7b99a83daed0f99bb37212ef22c70093aea50d4587b9a020576bd494d9ffc2c6053d51fe215cf8ae1765cd03a6de2534c5dc4b93dba8afa5674ad32ad4ae4cb306f3b62402'))
    print(f"plaintext: {plaintext}")


if __name__ == '__main__':
    main()

# proc.py (문제 제공 코드)
import random

class Affine:
    def __init__(self, key1, key2):
        assert isinstance(key1, int) and 1 <= key1 <= 250
        assert isinstance(key2, int) and 1 <= key2 <= 250
        self._key1 = key1
        self._key2 = key2

    def encrypt(self, msg):
        msg_enc = b""
        for b in msg:
            msg_enc += bytes([(self._key1 * b + self._key2) % 251])
        return msg_enc

def main():
    key1 = random.choice([k for k in range(1, 251) if pow(k, -1, 251) is not None])
    key2 = random.randint(1, 250)

    plaintext = ("The affine cipher is one of the classical encryption techniques used "
                 "in cryptography. It applies a linear transformation to each letter "
                 "in the plaintext using modular arithmetic. The encryption function "
                 "follows the formula: C = (a * P + b) mod m, where 'a' and 'b' are "
                 "secret keys. To decrypt, we use the modular inverse of 'a' to "
                 "reverse the transformation. While the affine cipher is simple, it "
                 "can be broken easily using frequency analysis. Nevertheless, it "
                 "serves as a great educational example of mathematical encryption "
                 "methods.\n\nNow, here comes the flag: SF{AffineC1ph3r_is_fun!}").encode()

    cipher = Affine(key1, key2)
    ciphertext = cipher.encrypt(plaintext)
    print(f"my encrypted sentence > {ciphertext.hex()}")
    print(f"Used keys (for validation): {key1}, {key2}")  # 문제 제공 시 제거

if __name__ == '__main__':
    main()
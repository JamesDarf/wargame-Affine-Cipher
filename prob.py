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
    # 랜덤한 적절한 key1, key2 선택
    key1 = random.choice([k for k in range(1, 251) if pow(k, -1, 251) is not None])
    key2 = random.randint(1, 250)
    
    # 암호화할 평문
    plaintext = ("The affine cipher is a classical encryption method that "
                 "applies a linear transformation to each letter using "
                 "modular arithmetic. It follows the formula: C = (a * P + b) mod m. "
                 "While simple, it can be broken using frequency analysis. "
                 "Nevertheless, it is an excellent example of mathematical encryption.\n\n"
                 "Now, here comes the flag: SF{AffineC1ph3r_is_fun!}").encode()
    
    cipher = Affine(key1, key2)
    ciphertext = cipher.encrypt(plaintext)
    
    # 암호문 출력
    print("Affine cipher? It's quite fine :>")
    print("No one can leak my secret sentence!")
    print(f"my encrypted sentence > {ciphertext.hex()}")
    
    # 문제 파일 제공 시 key1, key2는 출력하지 않음

if __name__ == '__main__':
    main()

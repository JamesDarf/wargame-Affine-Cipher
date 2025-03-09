# Affine-Cipher
# 🛠 Affine Cipher CTF 문제 해설

## 🔍 문제 개요
이 문제는 **Affine Cipher**(아핀 암호)를 이용한 클래식 암호학 문제다.  
주어진 **암호문(hex)** 을 복호화하여 평문과 플래그를 찾아야 한다.

## 🎯 암호화 방식
아핀 암호는 다음과 같은 수식을 따른다:

- **암호화:**  
  \[
  C = (a \times P + b) \mod 251
  \]
- **복호화:**  
  \[
  P = a^{-1} \times (C - b) \mod 251
  \]

여기서:
- \( P \) : 평문 문자(ASCII 값)
- \( C \) : 암호문 문자(암호화된 ASCII 값)
- \( a \), \( b \) : 비밀 키(암호화 키)
- \( a^{-1} \) : 모듈러 역원 (\( a \)의 251에 대한 역원)

## 🔑 문제 해결 과정

1. **암호문 확보**
   ```
   my encrypted sentence > 90b36f3568323276406f35e976c1b36f.......
   ```
   암호문이 16진수(hex)로 주어졌으므로, 이를 바이트로 변환한다.

2. **복호화 키 찾기**
   - `a`의 모듈러 역원(`a⁻¹ mod 251`)을 찾아야 함.
   - `b` 값을 맞춰서 암호문을 원래 평문으로 변환.

3. **복호화 코드 작성**
   다음은 암호문을 복호화하는 코드:

   ```python
   import binascii

   def modular_inverse(a, m):
       return pow(a, -1, m)  # 모듈러 역원 계산

   def affine_decrypt(ciphertext, a, b, m=251):
       a_inv = modular_inverse(a, m)
       return bytes([(a_inv * (c - b)) % m for c in ciphertext])

   # 암호문 (hex → bytes 변환)
   hex_ciphertext = "90b36f3568323276406f35e976c1b36f..."  # 문제에서 제공된 암호문
   ciphertext = bytes.fromhex(hex_ciphertext)

   # 문제에서 사용된 키 (해설에서는 제공, 실제 문제에서는 참가자가 찾아야 함)
   key1 = 148
   key2 = 36

   decrypted_text = affine_decrypt(ciphertext, key1, key2).decode(errors="ignore")
   print("복호화된 텍스트:", decrypted_text)
   ```

4. **복호화된 평문 확인**
   ```
   The affine cipher is one of the classical encryption techniques used in cryptography...
   
   Now, here comes the flag: SF{AffineC1ph3r_is_fun!}
   ```
   → 플래그는 **`SF{AffineC1ph3r_is_fun!}`** 🎉

## ✅ 결론
- Affine 암호는 수학적으로 단순하며, **모듈러 역원**을 사용해 복호화 가능하다.
- 모듈러 연산을 이해하고, 키를 분석하면 쉽게 풀 수 있는 문제다.
# Affine-Cipher

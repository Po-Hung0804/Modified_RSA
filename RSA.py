import random
from sympy import nextprime

def msd(num):
    ans = 0
    while num:
        ans += 1
        num >>= 1
    return ans

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t

def modular_pow(base, exponent, modulus):
    if modulus == 1:
        return 0
    result = 1
    base %= modulus
    while exponent:
        if exponent & 1:
            result = result * base % modulus
        exponent >>= 1
        base = base ** 2 % modulus
    return result

def modular_inverse(num, modulus):
    gcd, s, t = extended_gcd(num, modulus)
    if gcd != 1:
        return -1
    else:
        return s % modulus

def generate_prime(bit_length):
    return [nextprime(1 << bit_length - 1, i) for i in range(1, 101)]

def toprime(primes, n):
    return random.sample(primes, n)

def RSAnkey(n, primesbase):
    while True:
        N = 1
        phi = 1
        primes = toprime(primesbase, n)
        for prime in primes:
            N *= prime
            phi *= (prime - 1)
        
        while True:
            e = random.randint(2, phi)
            if gcd(phi, e) == 1:
                break
        
        d = modular_inverse(e, phi)
        if e != 1 and d != -1:
            break
    
    return e, N, d

def encrypt(public_key, plaintext):
    e, n = public_key
    plaintext_int = int.from_bytes(plaintext.encode('utf-8'), 'big')
    ciphertext = modular_pow(plaintext_int, e, n)
    return ciphertext

def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext_int = modular_pow(ciphertext, d, n)
    plaintext = plaintext_int.to_bytes((plaintext_int.bit_length() + 7) // 8, 'big').decode('utf-8')
    return plaintext

if __name__ == "__main__":
    print("How many keys needed to be used?")
    n = int(input())
    with open('primes.txt', 'r') as f:
        primesbase = [int(line.strip()) for line in f]
    e, N, d = RSAnkey(n, primesbase)
    # print(f"{N} primes:")
    # for prime in primes:
    #     print(prime)
    print(f"密鑰: {e} {N} {d}")
    print("please enter your plaintext:")
    plain = input()
    print(f"明文: {plain}")
    
    ciphertext = encrypt((e, N), plain)
    print(f"密文: {ciphertext:X}")
    
    decrypted = decrypt((d, N), ciphertext)
    print(f"解密文: {decrypted}")
    print(f"是否相同: {plain == decrypted}")

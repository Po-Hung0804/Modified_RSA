# Modified_RSA
## Introduction
This project demonstrates the implementation of an RSA cryptosystem using three prime numbers (`p`, `q`, `r`) and evaluates its security against factorization attacks. It includes key generation, encryption, decryption, and complexity analysis.

## Overview

In this implementation, RSA's modulus `n` is the product of three large prime numbers. The security of this scheme relies on the computational difficulty of factorizing `n`. For modern systems, factorizing a 3072-bit modulus with three primes is computationally infeasible using current technology.

### Key Features
- **Key Generation**: Generates a public-private key pair using three primes.
- **Encryption**: Encrypts plaintext using the public key.
- **Decryption**: Decrypts ciphertext using the private key.
- **Security Analysis**: Compares brute-force attack complexity for different RSA key lengths and configurations.

---

## Implementation Details
### Key Generation
- **Prime Generation**: Use the sympy library to generate a pool of prime numbers and save them in a file named prime.txt.
- **Select Primes**: Choose three distinct primes p, q, and r from the prime pool.
- **Calculate Modulus**: Compute n = p × q × r.
- **Euler's Totient**: Calculate φ(n) = (p-1) × (q-1) × (r-1).
- **Public Exponent**: Select e such that gcd(e, φ(n)) = 1.
- **Private Exponent**: Compute d such that e × d ≡ 1 (mod φ(n)).
### Keys:
- **Public Key**: (e, n)
- **Private Key**: d
### Encryption
`1. Input: Plaintext message M, public exponent e, and modulus n.`

`2. Output: Ciphertext C, calculated as C = M^e mod n.`
### Decryption
`1. Input: Ciphertext C, private exponent d, and modulus n.`

`2. Output: Plaintext M, calculated as M = C^d mod n.`

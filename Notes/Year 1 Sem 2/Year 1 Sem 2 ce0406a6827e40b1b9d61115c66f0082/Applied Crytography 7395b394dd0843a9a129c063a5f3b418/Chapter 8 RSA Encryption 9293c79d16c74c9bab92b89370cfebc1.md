# Chapter 8: RSA Encryption

Created: Jan 16, 2020 11:40 PM
URL: https://www.google.com/search?client=avast&q=phi+symbol
Updated: Feb 12, 2020 10:37 PM

**Private-Key Cryptography:**

- Traditional private/secret/single key cryptography uses one key only
- Key disclosed
    - Confidentiality of communications compromised
    - Repudiation of sender compromised

**Public-Key Cryptography:**

Details:

- Uses two keys, one public one private
    - Public known to anybody, used to encrypt messages and verify signatures
    - Private known only to recipient to decrypt and sign signatures
- Asymmetric, both parties are not using same key
    - Those who encrypt or verify cannot decrypt or create
- Complements private key cryptography
- Uses number theoretic concepts

Why Public-Key Cryptography?:

- Solves 2 key issues
    - Key distribution - Enable secure communications without having to trust a KDC with your key
    - Digital Signatures - Enables verification of a message from claimed sender

[Chapter%208%20RSA%20Encryption%209293c79d16c74c9bab92b89370cfebc1/untitled](Chapter%208%20RSA%20Encryption%209293c79d16c74c9bab92b89370cfebc1/untitled)

Characteristics:

- Easy to en/decrypt message when relevant key is known
- Hard to find decryption key
- Two related keys can be switched for encryption while the other must be used for decryption

[Chapter%208%20RSA%20Encryption%209293c79d16c74c9bab92b89370cfebc1/untitled%201](Chapter%208%20RSA%20Encryption%209293c79d16c74c9bab92b89370cfebc1/untitled%201)

Applications:

- Encryption/Decryption to provide secrecy (RSA)
- Digital Signatures to provide authentication (DSA)
- Key exchange (Diffie-Hellman)

Security of Public Key Schemes:

- Brute force attack is always theoretically possible
- Made hard enough to be impractical to break by using large keys
- Public key is slow compared to private key cryptography

**RSA:**

Details:

- Best known & most widely used public-key scheme
- Encryption/Decryption based on exponentiation
- Security of RSA is due to cost of factoring large numbers

Key Setup:

- Each user generates a key pair by selecting two large primes at random , "p" and "q"
- Compute their system modulus, "n = p*q"
- Compute "Φ(n) = (p-1)(q-1)"
- Select encryption key "e" where e is an odd integer that does not share same common factor as Φ(n)
- Find decryption key "d" by using d = k(Φ(n)+1)/e
- Publish public key "PU={e,n}"
- Keep private key "PR={d,n}"

How it works:

- Alice wants BOB to send a message, m = (number)
- Alice generates P1, P2 and N
- She then finds Φ(N)
- She then picks "e", where "e" is an odd number that does not share a common factor with Φ(N)
- She calculates "d" using the formula above
- Everything except "N" and "e" is kept secret
- She sends "N" and "e" to Bob
- Bob locks the message via calculating "m^e mod N" and sends back to Alice, this is c
- Alice decrypts using "c^d mod N" which gives m
- M must be smaller than n, break M into blocks if needed

**RSA Attacks:**

Brute Force:

- Given n, factor p.q compute Φ(N) to compute d
- Determine Φ(N) directly and compute d
- or even find d directly

Mathematical Attack on Factoring:

- Improvements in algorithms and Quantum Computers could break RSA
- Currently recommend n >= 2048 bits length

Misuse:

- Reusing the same N with different d & e is unsafe
- Use long private exponents to make brute force harder

Chosen Ciphertext Attack:

- Attacker sends cipher text and gets plaintext back
- Victim may not see the original cipher text
- Solution is to use random padding on plaintext

Timing Attacks:

- Based on time required by device to decrypt/sign
- Solution is to use delays in timing

Power Cryptanalysis:

- Based on power required by device during signature generation to discover secret key

**RSA Key Generation Considerations:**

- Select 2 sufficiently large primes to generate
- N should be > 2046 bits in length
- P and Q should be prime
- e and N should be co-prime
- Message must be smaller size than N
- Use bigger exponents when possible
- Use paddings such as OAEP
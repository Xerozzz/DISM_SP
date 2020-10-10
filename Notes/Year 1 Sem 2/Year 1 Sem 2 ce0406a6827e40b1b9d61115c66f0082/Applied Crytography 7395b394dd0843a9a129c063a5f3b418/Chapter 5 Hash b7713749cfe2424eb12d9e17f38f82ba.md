# Chapter 5: Hash

Created: Jan 31, 2020 9:14 PM
Updated: Feb 16, 2020 6:25 PM

**Content:**

- Different requirements of message security
- Hash Algorithm construction
- Overview of the SHA-2 core hash function
- Attacks
- The requirements of hash function in different applications

**Security != Encryption:**

Confidentiality:

- Attacks
    - Disclosure
    - Traffic Analysis
- Requirements
    - Adversary cannot understand decrypt the message

Authentication:

- Attacks
    - Masquerade
    - Content modification
    - Sequence modification
    - Timing modification
    - Source repudiation
    - Destination repudiation
- Authentication
    - Integrity of a message, has the messaged been changed or modified in transit?
    - Validate identity of the originator, ascertain the sender of the message
    - Non-repudiation of origin, recipient passes the message + proof to 3rd party to confirm the message originated from sender

**Encryption:**

Details:

- Strong encryption provides confidentiality
- Provides some authentication by using symmetric key encryption
    - Receiver assumed sender created message as only S and R know the key
    - Receiver assumed message content unaltered as altering encrypted message will corrupt it

Using Public-Key Encryption:

- Encryption provides no information of sender
- In public key system, sender can signs message under their private-key then encrypts with recipient's public key
- Provides both secrecy and authentication
- Notes: 2 pairs of public-private keys used

**Hash Algorithm:**

Requirements:

[Chapter%205%20Hash%20b7713749cfe2424eb12d9e17f38f82ba/untitled](Chapter%205%20Hash%20b7713749cfe2424eb12d9e17f38f82ba/untitled)

Merkle-Damgard Construction:

- Sort of like Chained Block Cipher
- Append padding and length to message
- Break input into equal-sized blocks (512 or 1024 bits)
- Apply compression function f iteratively
- Proven collision resistant if Hash Function F is collision resistant
- Hashing algorithm (MD5,SHA1 etc) uses a different hash function but based on same Merkle-Damgard construction concept

[Chapter%205%20Hash%20b7713749cfe2424eb12d9e17f38f82ba/untitled%201](Chapter%205%20Hash%20b7713749cfe2424eb12d9e17f38f82ba/untitled%201)

![Chapter%205%20Hash%20b7713749cfe2424eb12d9e17f38f82ba/Annotation_2020-01-31_212918.jpg](Chapter%205%20Hash%20b7713749cfe2424eb12d9e17f38f82ba/Annotation_2020-01-31_212918.jpg)

Known Hash Algorithms:

- MD4 and MD5 by Ron Rivest
- SHA-0, SHA-1 by NSA
- SHA-2
- SHA-3
- Whirlpool
- Tiger

Simple Hash Functions:

- Based on XOR of message blocks and rotate bits
- Insecure as predictable effect on digest and non collision resistant
- If message is not encrypted, easy to modify the message and append one block that would set hash code as needed

Secure Hash Algorithm (SHA):

- Designed by NIST and NSA in 1993
- Based on design of hash function MD4 but produces 160-bit hash values

Revised Secure Hash Algorithm (SHA-2):

- Six versions of SHA-2
    - SHA-224,SHA-256,SHA-384,SHA-512
    - SHA-512/224,SHA-512/256
- Designed for compatibility and increased security
    - Structure and detail similar to SHA-1
    - Analysis should be similar
    - Much higher security

Processing of SHA-512:

- Overview
- Processing of SHA-512
    - Step 1: Append padding to bits
    - Step 2: Append length of the message
    - Step 3: Initialize hash buffers
    - Step 4: Process the message in 1024-bit blocks
    - Step 5: Output the final state value as the resulting hash

[Chapter%205%20Hash%20b7713749cfe2424eb12d9e17f38f82ba/untitled%202](Chapter%205%20Hash%20b7713749cfe2424eb12d9e17f38f82ba/untitled%202)

[Chapter%205%20Hash%20b7713749cfe2424eb12d9e17f38f82ba/untitled%203](Chapter%205%20Hash%20b7713749cfe2424eb12d9e17f38f82ba/untitled%203)

[Chapter%205%20Hash%20b7713749cfe2424eb12d9e17f38f82ba/untitled%204](Chapter%205%20Hash%20b7713749cfe2424eb12d9e17f38f82ba/untitled%204)

[Chapter%205%20Hash%20b7713749cfe2424eb12d9e17f38f82ba/untitled%205](Chapter%205%20Hash%20b7713749cfe2424eb12d9e17f38f82ba/untitled%205)

**Attacks:**

Preimage Resistance:

- Easy to generate a code given a message, but virtually impossible to generate a message given a code
- Given y, it is difficult to find an x such that h(x) = y

Second Preimage Resistance:

- Computationally infeasible to find a pair of messages with the same hash value
- Given x, it is difficult to find a second preimage x' != x such that h(x) = h(x')

Birthday Attack:

- General purpose attack on Hash functions
- Higher likelihood of collisions found between random attack attempts and a fixed degree of permutations

Problem Statements:

- What is the probability that any two students in a class have the same birthday when there are 23 students in a class? 50%

**Application of Hash Algorithms:**

Public Key Algorithms:

- Password Logins
- Encryption Key Management
- Digitial Signatures

Integrity Checking:

- Virus and Malware Scanning

Authentication:

- Secure Web Connections (PGP, SSL, SSH)

[Chapter%205%20Hash%20b7713749cfe2424eb12d9e17f38f82ba/untitled%206](Chapter%205%20Hash%20b7713749cfe2424eb12d9e17f38f82ba/untitled%206)
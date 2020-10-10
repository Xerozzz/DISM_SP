# Chapter 9: Key Distribution & Diffie-Hellman Key Exchange

Created: Feb 6, 2020 11:59 PM
Updated: Feb 13, 2020 8:41 PM

**Distribution of Public Keys:**

Problem:

- How to distribute keys securely
- Why is there a need to distribute secret keys with aid of public key
- How Diffie-Hellman Key Exchange works

1. Public Announcement:

- Users distribute public keys to recipients or broadcast to community at large
    - Append PGP keys to email messages and send across netowrk
    - Post PGP keys on news group or email list
    - Various sites support posting PGP key as part of user profile
    - Convenient and works well for small scale distribution
- Weakness
    - Forgery - Anyone can create a key claiming to be someone else and broadcast it
    - Adversary can masquerade as claimed user until discovered

2. Publicly Available Directory:

- Directory must be trusted with properties
    - Contains name and public key entries
    - Participants register securely with directory
    - Participants can replace key at any time
    - Directory is periodically published
    - Directory can be accessed electronically
    - Directory must be trusted
- Greater security compared to method 1 but still vulnerable to tampering or forgery
    - Attacker pretends to be authorised directory or changes records in directory

3. Public Key Authority:

- Improved security and tighten control over distribution of keys from directory
- Central Authority maintains a dynamic directory of public keys of all participants
- Requirements
    - Authority must be secured
    - All users must know public key of authority with only authority knowing knowing the corresponding private key
    - Real-time access to directory when keys are needed
- Issues
    - Authority can become bottleneck
    - Records maintained can also be tempered with

![Chapter%209%20Key%20Distribution%20&%20Diffie-Hellman%20Key%20Ex%207f2fd1ceb7544b56a39dbded6e51b107/Annotation_2020-02-07_151455.jpg](Chapter%209%20Key%20Distribution%20&%20Diffie-Hellman%20Key%20Ex%207f2fd1ceb7544b56a39dbded6e51b107/Annotation_2020-02-07_151455.jpg)

4. Public-Key Certificates:

- To overcome bottleneck in 3, we can use Public-Key Certificates
    - Allows key exchange without real-time access to public-key authority
    - Binds identity to public key
- Public-Key signed by a trusted Certificate Authority can be verified by anyone
- Certificate Authority's public-key is publicly available

[Chapter%209%20Key%20Distribution%20&%20Diffie-Hellman%20Key%20Ex%207f2fd1ceb7544b56a39dbded6e51b107/untitled](Chapter%209%20Key%20Distribution%20&%20Diffie-Hellman%20Key%20Ex%207f2fd1ceb7544b56a39dbded6e51b107/untitled)

***M1 & M3:***

•*Users store public keys with CA*

***M2 & M4:***

•*CA provides certificates to users*

•*Certificate is a document contains user’s public key, CA’s signature, time stamp(validity of cert.) as well as identity of user*

When A and B want to communicate, the only message that need to be sent is (1) and (2)

•M1 to M4 happen in advance way before message (1) and (2)

•This is why the performance is improved greatly as now only (1) and (2) is required for A and B to exchange message. No message goes to Authority during communication

•Certificates exchange between A and B is issued by Certificate Authority or CA

***M1 & M3:***

•*Users store public keys with CA*

***M2 & M4:***

•*CA provides certificates to users*

•*Certificate is a document contains user’s public key, CA’s signature, time stamp(validity of cert.) as well as identity of user*

•CA not involved in communication

•Certificates received are verified using CA’s public key

Key Exchange:

- Public-Key encryption needs to be long to be hard to break, which can be CPU intensive or slow
- Alternatively, use a secure way to exchange a secret key to do secret key encryption

**Diffie-Hellman Key Exchange:**

Details:

- First public-key scheme proposed in 1976 by Diffie and Hellman
- DH is not for data secrecy or authentication
- It is a practical method for public exchange of a secret key

[Chapter%209%20Key%20Distribution%20&%20Diffie-Hellman%20Key%20Ex%207f2fd1ceb7544b56a39dbded6e51b107/untitled%201](Chapter%209%20Key%20Distribution%20&%20Diffie-Hellman%20Key%20Ex%207f2fd1ceb7544b56a39dbded6e51b107/untitled%201)

Features:

- Establish a common key known only to the two participants
    - Value of key depends on the participants
- Cannot be used to exchange an arbitrary message
- Should be
    - Computationally easy to forward process exponential modulo a prime or polynomials
    - Computationally hard to reverse process using discrete logarithms

Setup:

- All users need to agree on global parameters p (large prime integer) and g (primitive root modulo of p)

![Chapter%209%20Key%20Distribution%20&%20Diffie-Hellman%20Key%20Ex%207f2fd1ceb7544b56a39dbded6e51b107/Annotation_2020-02-07_001337.jpg](Chapter%209%20Key%20Distribution%20&%20Diffie-Hellman%20Key%20Ex%207f2fd1ceb7544b56a39dbded6e51b107/Annotation_2020-02-07_001337.jpg)

![Chapter%209%20Key%20Distribution%20&%20Diffie-Hellman%20Key%20Ex%207f2fd1ceb7544b56a39dbded6e51b107/Annotation_2020-02-07_001347.jpg](Chapter%209%20Key%20Distribution%20&%20Diffie-Hellman%20Key%20Ex%207f2fd1ceb7544b56a39dbded6e51b107/Annotation_2020-02-07_001347.jpg)

- Kab is the session key in private key encryption scheme between Alice and Bob
- Subsequent communications between Alice and Bob will have same key as before
- Attacker must solve discrete log to get Xa or Xb

Example:

[Chapter%209%20Key%20Distribution%20&%20Diffie-Hellman%20Key%20Ex%207f2fd1ceb7544b56a39dbded6e51b107/untitled%202](Chapter%209%20Key%20Distribution%20&%20Diffie-Hellman%20Key%20Ex%207f2fd1ceb7544b56a39dbded6e51b107/untitled%202)

**Key Exchange Protocols:**

- If the public-key is properly secured in a central directory (aka with PKI)
    - Other users could query the public-key to compute the secret key to communicate
    - Authentication of user is possible using PKI (Public Key Infrastructure)
- Diffie-Hellman Exchange Attack
    - Replay Attacks (with/without PKI)
    - Man-in-the-Middle Attacks (without PKI)
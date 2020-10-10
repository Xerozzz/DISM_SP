# Chapter 7: Cryptographic Hash

Created: Feb 2, 2020 10:17 PM
Updated: Feb 20, 2020 11:24 AM

**Content:**

- Function, requirements and application of digital signatures
- How is digital signature implemented
- Type of digital signatures
- Digital Signature Scheme and standard

**Digital Signature:**

Details:

- Provides message authentication through Hash, MAC or encryption
- Does not address issues of lack of trust
- Signature provides
    - Authentication of message content
    - 3rd parties verification
    - Non-Repudiation

Requirements:

- Must be a bit pattern that depend on message signed
- Must be information unique to sender
- Must be relatively easy to produce
- Must be relatively easy to recognise and verify
- Should be computationally infeasible to forge
- Should be practical to save digital signature in storage

Application:

- Used to sign documents, emails (eg. PDF,WORD)
- Used to sign server's certificate
- Provide online signing services (eg. DocuSign)

How it works:

- Digital Signature is an authentication mechanism that enables the creator of a message to attach a code that acts as a signature
- The signature is formed by taking the hash of the message and encrypting the message with the creator's private key
- The signature guarantees the source and integrity of the message
- The signature verifies the sender, authenticates message content and helps solve third party disputes

**Type of Digital Signature:**

Direct Digital Signatures:

- Involves only sender and receiver
    - Each have their own private-public key pair
    - Each have the other's public key
- Sign first using sender's priv key then encrypt message and signature
    - Either encrypts entire message or
    - encrypt hash only for efficiency
- Encrypts using receiver's public key
- Validity depends on sender's private key

Arbitrated Digital Signatures:

- Implementing an arbitrated digital signature invites a third party into the process called a "trusted arbiter"
- Use of an arbiter (3rd party)
    - Arbiter receive signed messages from sender
    - Validate content & origin from subject, message and signature
    - Arbiter dated the message and indicated the message have been verifed
    - Sent to recipient
- Arbiter may or may not see the message
- Suitable level of trust in arbiter required
- Implemented together with private or public encryption
    - Needs complete trust from both sender and receiver that the arbiter follow as instructed and not alter data in any way
    - Prevent sender from disowning messages

**Digital Signature Schemes:**

Algorithms:

- Key generation algorithm to randomly select a key pair
- Signature algorithm - Message + Private Key = Signature
- Signature Verification Algorithm - Public key + Signature = True/False

Digital Signature Standard (DSS):

- US Govt approved signature scheme
- Uses the SHA hash algorithm
- DSS is the standard, DSA is the algorithm

Digital Signature Algorithm (DSA):

- Based on Asymmetric Key Algorithm
- A digital signature scheme
    - 320-bit signature length
    - 512-1024 bit security key
- Smaller & faster than RSA
- Security = discrete logarithm (computationally hard problem)

[Chapter%207%20Cryptographic%20Hash%209ace9415179d4c439169a209255daf2d/untitled](Chapter%207%20Cryptographic%20Hash%209ace9415179d4c439169a209255daf2d/untitled)
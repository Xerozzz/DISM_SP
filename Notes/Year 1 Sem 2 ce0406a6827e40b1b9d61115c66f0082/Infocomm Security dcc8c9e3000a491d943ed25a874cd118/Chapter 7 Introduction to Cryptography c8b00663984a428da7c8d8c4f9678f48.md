# Chapter 7: Introduction to Cryptography

Created: Feb 3, 2020 1:09 PM
Updated: Mar 1, 2020 6:54 PM

**Objectives:**

- Define cryptography
- Define hash, symmetric, and asymmetric cryptographic algorithms
- Explain different cryptographic attacks
- List the various ways in which cryptography is used

**Defining Cryptography:**

- Understand what it is
- Understand what it can doUnderstand how it can be used as security tool

**What is Cryptography?**

Cryptography:

- Scrambling information so it cannot be read
- Transforms information into secure form so unauthorized persons cannot access it

Steganography:

- Hides the existence of data
- An image,audio or video file can contain hidden embedded messages
- Archived by dividing data and hiding in unused portions of file
- May hide data in file metadata

Details:

- Modern cryptographic algorithms rely upon underlying mathematical formulas and the quality of random numbers
- Software relies upon a pseudo-random number generator (PRNG)
- Two factors to thwart threat actors from discovering underlying key to algorithms
    - Diffusion - If a single character of plaintext is changed then it should result in multiple characters of the ciphertext changing
    - Confusion - The key does not relate in a simple way to the ciphertext

**Cryptography and Security:**

Confidentiality:

- Ensures only authorized parties can view it
- Encrypted information can only be viewed by those who have the key

Integrity:

- Ensures information is correct and unaltered
- Encrypted information cannot be changed except by authorized users who have the key

Authentication:

- Ensures sender can be verified through cryptography
- Proof that the sender was legitimate and not an impostor can be obtained

Non-repudiation:

- Proves that a user performed an action
- Individuals prevented from fraudulently denying threat they were involved in a transaction

Obfuscation:

- Making something obscure or unclear
- By hiding the details the original cannot be determined

Security through Obscurity:

- An approach in security where virtually any system can be made secure as long as outsiders are unaware of it or how it function

Three states of data:

- Data in use
    - Data actions being performed by endpoint devices
- Data-in-transit
    - Actions that transmit the data across a network
- Data-at-rest
    - Data stored on electronic media

**Cryptography Constraints:**

Details:

- The number of small electronic devices has grown significantly
- These devices need to be protected from threat actors
- Applications require extremely fast response times also face cryptography limitations
- It is important to have high resiliency in cryptography to quickly recover from constraints

Resource vs Security Constraint:

- A limitation in providing strong cryptography due to the tug-of-war between available resources and the security provided by cryptography

**Cryptographic Algorithms:**

Amount of Data Processed at a time:

- **Stream Cipher** - Takes one character and replaces it with another
- **Block Cipher** - Manipulates an entire block of plaintext at one time
- **Sponge Function** - Takes as input a string of any length and returns a string of any requested variable length

Cryptographic Algorithms:

- Hash Algorithms
- Symmetric Cryptographic Algorithms
- Asymmetric Cryptographic Algorithms

**Hash Algorithms:**

Details:

- Creates a unique "digital fingerprint" of a set of data and is commonly called hashing
- This fingerprint, called a digest represents the contents
- Contents cannot be used to reveal original data set
- Primarily used for comparison purposes to ensure original data is unaltered
- Hashing is intended to be one way in that the digest cannot be reversed to reveal original data

Characteristics:

- Fixed Size - Short and long data sets have the same size hash
- Unique - Two different data sets cannot produce the same hash
- Original - Data set cannot be created to have a predefined hash
- Secure - Resulting hash cannot be reversed into original plaintext

Hash Example:

- Bank customer has PIN of 93542
- Number is hashed and stored on card's stripe
- User inserts card in ATM and enters PIN
- ATM hashes the PIN using same algo
- If two values match, user may access ATM

Message Digest 5 (MD5):

- Most well-known of the MD hash algorithms
- Message length padded to 512 bits
- Weaknesses in compression function could lead to collisions
- Some security experts recommend using a more secure hash algorithm

Secure Hash Algorithm (SHA):

- More secure than MD
- SHA-2 is currently considered to be a secure hash
- SHA-3 was announced as a new standard in 2015 and may be suitable for low-power devices

Race Integrity Primitives Evaluation Message Digest (RIPEMD):

- Primary design feature is two different and independent parallel chains of computation
- Results are combined at end of process
- Several Versions- RIPEMD-128,256,320

Hashed Message Authentication Code (HMAC):

- Hashed version providing improved security
- Uses a shared secret key possessed by sender and receiver
- Receiver uses a key to decrypt the hash

**Symmetric Cryptographic Algorithms:**

Details:

- Uses a single key to encrypt and decrypt a document
- Private key crytography
- Common algorithms
    - Data Encryption Standard (DES)
    - Triple Data Encryption Standard (3DES)
    - Advanced Encryption Standard (AES)
    - Several others

Data Encryption Standard (DES):

- Based on product originally designed in early 1970s
- Uses a 56-bit key and is a block cipher

Triple Data Encryption Standard (3DES):

- Designed to replace DES
- Uses three rounds of encryption
- Ciphertext of first round becomes input for second iteration and so forth
- Most secure versions use diff keys for each round

Advanced Encryption Standard (AES):

- A symmetric cipher approved by the NIST in 2000 as replacement for DES
- Performs three steps on every block (128-bits) of plaintext
- Designed to be secure well into the future

Other Algorithms:

- Rivest Cipher (RC)
    - Family of cipher algorithms designed by Ron Rivest
- Blowfish
    - Block cipher operating on 64-bit blocks with key length from 32-448 bits
    - No significant weaknesses have been identified
- International Data Encryption Algorithm (IDEA)
    - Used in European Nations
    - Block cipher processing 64-bits with a 128-bit key with 8 rounds

**Asymmetric Cryptographic Algorithms:**

Weaknesses:

- Distributing and maintaining a secure single key among multiple users distributed geographically

Components:

- Also known as public key cryptography
- Uses two mathematically related keys
- Public key available to everyone and freely distributed
- Private key known only to individual to whom it belongs

Common Asymmetric Cryptographic Algorithms:

- RSA
- Elliptic Curve Cryptography
- Digital Signature Algorithm
- Those relating to Key Exchange

RSA:

- Published in 1977 and patented by MIT in 1983
- Most common asymmetric cryptography algo
- Uses two large prime numbers

Elliptic Curve Cryptography (ECC):

- Users share one elliptic curve and one point on the curve
- Uses less computing power than prime number-based asymmetric cryptography as key sizes are smaller
- Considered as alternative for mobile and wireless devices

[Chapter%207%20Introduction%20to%20Cryptography%20c8b00663984a428da7c8d8c4f9678f48/untitled](Chapter%207%20Introduction%20to%20Cryptography%20c8b00663984a428da7c8d8c4f9678f48/untitled)

Digital Signature Algorithm (DSA):

- Digital Signature - and electronic verification
- Verifies the sender
- Prevents sender from disowning the message
- Proves message integrity

[Chapter%207%20Introduction%20to%20Cryptography%20c8b00663984a428da7c8d8c4f9678f48/untitled%201](Chapter%207%20Introduction%20to%20Cryptography%20c8b00663984a428da7c8d8c4f9678f48/untitled%201)

**Cryptographic Attacks:**

More common attacks:

- Target algorithm weaknesses
- Exploit collisions

**Algorithm Attacks:**

Methods:

- Known ciphertext attacks
- Downgrade attacks
- Using deprecated algorithms
- Improper implementations

Known Ciphertext Attack:

- Statistical tools can be used to attempt to discover a pattern in ciphertext, which can then be used to reveal plaintext and/or key

[Chapter%207%20Introduction%20to%20Cryptography%20c8b00663984a428da7c8d8c4f9678f48/untitled%202](Chapter%207%20Introduction%20to%20Cryptography%20c8b00663984a428da7c8d8c4f9678f48/untitled%202)

Downgrade Attack:

- A threat actor forces the system to abandon the current higher security mode of operation and instead "fall back" to implementing an older and less secure mode

Using Deprecated Algorithms:

- Means to use a cryptographic algorithm that should not be used because of known vulnerabiltiies

Improper Implementations:

- Known as misconfiguration implementation
- Many cryptographic algorithms have several configuration options
- Unless careful consideration is given to these options the cryptography may be improperly implemented

**Collision Attacks:**

Details:

- An attempt to find two input strings of a hash function that produce the same hash result

Birthday Attacks:

- Based on birthday paradox, which says that for there to be a 50 percent chance that someone in a given room share your birthday, 253 people would need to be present

**Using Cryptography:**

Should be used to secure:

- Data-in-transit
- Data-at-rest
- Data-in-use
- Individual files and databases
- Removable media
- Data on mobile devices

Applied through:

- Software
- Hardware

**Encryption Through Software:**

File and File System Cryptography:

- Encryption software can be used to encrypt or decrypt files one-by-one

Pretty Good Privacy (PGP):

- Widely used asymmetric cryptography system
- Used for files and e-mails on Windows systems
- GNU Privacy Guard (GNuPG)
    - Open source product that runs on Windows, UNIX and Linux operating systems
- OpenPGP is another open-source alternative that is based on PGP

Operating System Encryption:

- Microsoft Windows Encrypting File System (EFS)
- Cryptography system for Windows
- Uses NTFS file system
- Tightly integrated with file system
- Encryption and decryption transparent to user

Full Disk Encryption (FDE):

- Protects all data on a hard drive
- Eg. BitLocker - drive encryption software that is included in Microsoft Windows
- BitLocker encrypts entire system volume including Windows Registry
- Prevents attackers from accessing data by booting from another OS or placing the hard drive in another computer

**Encryption Through Hardware:**

Details:

- Software encryption can be subject to attacks to exploits its vulnerabilities
- Cryptography can be embedded in hardware to provide higher degree of security in USB and standard hard drive devices
- Hardware Encryption Options
    - Trusted Platform Module
    - Hardware Security Model

USB Device Encryption:

- Encrypted hardware-based flash drives can be used
- Will not connect a computer until correct password is entered
- All data copied to the drive is automatically encrypted
- Tamper-resistant external cases
- Administrators can remotely control and track activity on the devices
- Stolen drives can be remotely disabled

Self-Encrypting Drives (SEDs):

- Self-encrypting hard disk drives protect all files stored on them
- The drive and host device perform authentication process during initial power up
- If authentication fails, the drive can be configured to deny access or even delete encryption keys so all data is permanently unreadable

Trusted Platform Module (TPM):

- A chip on a computer's motherboard that provides cryptographic services
- Includes a true random number generator
- Entirely done in hardware it cannot be subject to a software attack
- Prevents computer from booting if files or data have been altered
- Prompts for password if hard drive moved to a new computer

Hardware Security Module (HSM):

- A secure cryptographic processor
- Includes an onboard key generator and key storage facility
- Performs accelerated symmetric and asymmetric encryption
- Can provide services to multiple devices over a LAN
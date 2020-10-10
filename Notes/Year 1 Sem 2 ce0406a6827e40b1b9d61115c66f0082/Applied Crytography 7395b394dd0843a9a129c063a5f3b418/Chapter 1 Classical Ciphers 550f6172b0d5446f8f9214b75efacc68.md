# Chapter 1: Classical Ciphers

Created: Jan 22, 2020 10:49 PM
Updated: Feb 3, 2020 11:39 AM

**Content:**

- Cryptology
    - Cryptography
    - Cryptanalysis
- Steganography
- Classical Ciphers
- Rotor Machines

**Cryptography:**

Categorized by:

- Type of encryption operations used
    - Substitution
    - Transposition
    - Product (Both of the above)
- Number of keys used
    - Single/Secrete
    - Two/Public
- Way which plaintext is processed
    - Stream (One element at a time)
    - Block (Block of elements)

Symmetric Encryption:

- Single-key encryption
- Sender and receiver share common key
- All classical encryption are symmetric key algorithms
- One key to encrypt and decrypt
- Must be a strong encryption algorithm
- Secret key can only be known my S and R
- Requires a secure channel to distribute key

**Cryptanalysis:**

General Approaches:

- Brute Force
    - Try all possible keys
- Cryptanalytic attack
    - Based on nature of algorithm
    - General characteristic of plaintext
    - sample of plaintext-ciphertext pairs
- Objective of attacking encryption system is to recover key in use instead of simply recovering plaintext from ciphertext

Terminology:

- Unconditional security (Ideal)
    - No matter how much computer power or time there is, cipher cannot be broken as ciphertext provides insufficient information to determine plaintext
- Computational Security (Realistic)
    - Given limited computing resources, cipher cannot be broken

Attacks:

- Ciphertext only
    - Only know algo and ciphertext (hardest)
- Known plaintext
    - Know/suspect plaintext & ciphertext
- Chosen plaintext
    - Select plaintext and obtain ciphertext
- Chosen ciphertext
    - Select ciphertext and obtain plaintext
- Chosen text
    - Select plaintext or ciphertext to en/decrypt

Brute Force Search:

- Try every possible key
- Most basic attack , proportional to key size
- Assume either know/recognize plaintext

One-Time Pad:

- Unbreakable as ciphertext bears no statistical relationship to plaintext
- Practical difficulties in generation and safe distribution of the key that is only used once, hence uncommon today
- Preconditions:
    - Key must be as long as plain text
    - Key must be truly random
    - Key can only be used once

Steganography:

- Alternative to encryption
- Hides the existence of a message
    - Use only subset of letters/words
    - Using invisible ink
    - Hiding info in LSB in graphic image or sound file
- Drawbacks
    - High overhead to hide relatively few info bits

**Substitution Cipher:**

- Letters of plaintext replaced by other letters,numbers or symbols
- Replacing plaintext bit patterns with ciphertext bit patterns

Caesar Cipher:

- Earliest known substitution cipher
- By Julius Caesar
- First used in military affairs
- Replaces each letter by 3rd letter up

Monoalphabetic Cipher:

- Maps each plaintext letter to a different random ciphertext letter
- Key is 26 letters long
- Can be any permutation of 26 alphabetic characters

![Chapter%201%20Classical%20Ciphers%20550f6172b0d5446f8f9214b75efacc68/Annotation_2020-01-22_231158.jpg](Chapter%201%20Classical%20Ciphers%20550f6172b0d5446f8f9214b75efacc68/Annotation_2020-01-22_231158.jpg)

Playfair Cipher:

- Encrypting multiple letters to solve regularities of language
- 5x5 matrix of letters based on key
- Uses I/J interchangeably and fills up matrix with remaining letters
- Eg. Using key MONARCHY

![Chapter%201%20Classical%20Ciphers%20550f6172b0d5446f8f9214b75efacc68/Annotation_2020-01-22_231333.jpg](Chapter%201%20Classical%20Ciphers%20550f6172b0d5446f8f9214b75efacc68/Annotation_2020-01-22_231333.jpg)

- Encrypting and Decrypting
    - If a pair is repeated letter, insert filler like "X" (hello -> helxlo)
    - If both letters in same row, replace each with letter to right, wrap around if needed (AR -> RM)
    - If both letters in same column, replace with letter below and wrap to top if needed (MU -> CM)
    - Otherwise, each letter replaced by letter in same row and column of pair (HS -> BP and EA -> IM/JM)
- Security
    - Much more improved over monoalphabetic (676 entries to 26 in monoalphabetic)
    - Harder to analyse
    - Can be broken given a few hundred letter as it has much of plaintext structure

Polyalphabetic Cipher:

- Same plaintext replaced by different ciphertext alphabets
    - Eg. BEE -> FHG
- Makes cryptanalysis harder with more guessing and flatter frequency distribution
- Key selects which ciphertext alphabet used to sub each letter of message

Vigenere Cipher:

- Simplest polyalphabetic substitution ciper
- Align plaintext and key, repeat key to match plaintext length

![Chapter%201%20Classical%20Ciphers%20550f6172b0d5446f8f9214b75efacc68/Annotation_2020-01-22_232138.jpg](Chapter%201%20Classical%20Ciphers%20550f6172b0d5446f8f9214b75efacc68/Annotation_2020-01-22_232138.jpg)

![Chapter%201%20Classical%20Ciphers%20550f6172b0d5446f8f9214b75efacc68/Annotation_2020-01-22_232220.jpg](Chapter%201%20Classical%20Ciphers%20550f6172b0d5446f8f9214b75efacc68/Annotation_2020-01-22_232220.jpg)

**Transposition Cipher:**

- Rearranges letter order without changing actual letters used
- Weak due to frequency distribution

Rail Fence Cipher:

- Write message letters out diagonally over a number of rows

![Chapter%201%20Classical%20Ciphers%20550f6172b0d5446f8f9214b75efacc68/Annotation_2020-01-22_232416.jpg](Chapter%201%20Classical%20Ciphers%20550f6172b0d5446f8f9214b75efacc68/Annotation_2020-01-22_232416.jpg)

Row Transposition Cipher:

- Write letters of the message out in rows over specified number of columns

**Rotor Machine:**

- Most complex ciphers in use during WW2
- Used a series of cylinders, each giving one substitution which rotated and changed after each letter was encrypted
- 3 cylinders have 26^3 alphabets

**Product Cipher:**

- More secure than simply just using substitution or transposition
- Uses both S and T, or 2 instances of either
- More S or T -> More complex
- Harder cipher created
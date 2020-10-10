# Chapter 2: DES

Created: Jan 24, 2020 3:01 PM
Updated: Feb 5, 2020 9:02 PM

**Content:**

- Block and stream ciphers
- scheme for cipher design
    - S-P network
    - Feistel Networks
    - Others
- DES Structure

**Block vs Stream Ciphers:**

Stream:

- Process messages a bit or byte at a time when en/decrypting

Block:

- Process messages in blocks, typical block size is 64 or 128 bits when en/decrypting
- Most current ciphers are block ciphers
    - Broader range of applications
    - Allows more complex designs
- Principles
    - Substitution-Permutation networks
    - Feistel Scheme

Substitution-Permutation Networks:

- Provide confusion and diffusion of message and key
    - Diffusion - Seeks to make statistical relationship between plaintext and ciphertext as complex as possible
    - Confusion - Makes relationship between ciphertext and key as complex as possible
- AES standard uses iterated S-P networks for En/decryption
- Cipher should completely obscure statiscal properties of original message

Feistel Scheme:

- Widely used to illustrate block cipher design principles
- Used in DES
- Once most widely used cryptographic algorithm
- Proven secrecy
- Considerations
    - Block and key size
    - Sub-key generation algorithm
    - Round (F) function
    - Number of rounds
- Construction of Feistel Cipher
    - Split input block into two halves
    - Use data from right half and apply substitution + sub key
    - XOR with the left half
    - Swap halves for the next cycle
    - Data on right side remains unchanged
    - F function performs S-box and P-box
    - After 2 rounds, data is encrypted 1 time

[Chapter%202%20DES%201ed2f774ffc34fecacb2c4a7041b0fa7/untitled](Chapter%202%20DES%201ed2f774ffc34fecacb2c4a7041b0fa7/untitled)

- Decryption
    - Reverse the subkeys applied

**Data Encryption Standard (DES):**

- Encrypts 64-bit blocks of data with 56-bit key
- Currently broken due to 56-bit key being brute forceable
- Heavily used in legacy and financial applications
- Splits the 64-bit block into two 32-bit parts

Encryption Steps:

- Initial Permutation (IP)
- 16 key dependent round functions (encrypts 8 times)
- Final permutation
- IP and FP are inverse of each other

[Chapter%202%20DES%201ed2f774ffc34fecacb2c4a7041b0fa7/untitled%201](Chapter%202%20DES%201ed2f774ffc34fecacb2c4a7041b0fa7/untitled%201)

--------------------------------------------------------------

[Chapter%202%20DES%201ed2f774ffc34fecacb2c4a7041b0fa7/untitled%202](Chapter%202%20DES%201ed2f774ffc34fecacb2c4a7041b0fa7/untitled%202)

(F) Round Structure:

- Expands R from 32 into 48-bit using expansion P-box function
- XOR with 48-bits subkey K
- Passes through 8 S-boxes to get 32-bit result
- Permutes using 32-bit P-box function

[Chapter%202%20DES%201ed2f774ffc34fecacb2c4a7041b0fa7/untitled%203](Chapter%202%20DES%201ed2f774ffc34fecacb2c4a7041b0fa7/untitled%203)

Substitution Boxes S:

- 8 different S-boxes working in parallel
- Map 6 to 4 bits (hence 48-32 bits)
- Value in the selected C of the S-Box is returned after process
- Bits 1 and 6 are row bits
- Bits 2-5 are col bits
- Eg. S5(011011) -> 9

[Chapter%202%20DES%201ed2f774ffc34fecacb2c4a7041b0fa7/untitled%204](Chapter%202%20DES%201ed2f774ffc34fecacb2c4a7041b0fa7/untitled%204)

Decryption:

- With feistel design, do encryption steps again with subkeys in reverse order

Key Schedule:

- Generate 16 subkeys from secret key
- Use PC-1 for IP
- Only 56-bits used (bit 8,16,24,32,40,48,56,64 are parity bits)
- 56-bit key is split into 2 halves of 28-bit
- Left shifts the bits one place to the left and wrap around
- Use PC-2 for permutation and select 48 bits from 56 bits

[Chapter%202%20DES%201ed2f774ffc34fecacb2c4a7041b0fa7/untitled%205](Chapter%202%20DES%201ed2f774ffc34fecacb2c4a7041b0fa7/untitled%205)

[Chapter%202%20DES%201ed2f774ffc34fecacb2c4a7041b0fa7/untitled%206](Chapter%202%20DES%201ed2f774ffc34fecacb2c4a7041b0fa7/untitled%206)

[Chapter%202%20DES%201ed2f774ffc34fecacb2c4a7041b0fa7/untitled%207](Chapter%202%20DES%201ed2f774ffc34fecacb2c4a7041b0fa7/untitled%207)

Considerations:

- Brute force search was previously hard (2^56 tries)
- Must be able to recognise plaintext
- DES is no longer reliable
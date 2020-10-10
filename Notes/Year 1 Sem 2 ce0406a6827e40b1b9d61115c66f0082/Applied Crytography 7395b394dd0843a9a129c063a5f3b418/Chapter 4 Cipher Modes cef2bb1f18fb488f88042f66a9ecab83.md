# Chapter 4: Cipher Modes

Created: Jan 30, 2020 10:43 PM
Updated: Feb 8, 2020 10:36 AM

**Content:**

- Shortfalls of using plain cipher
- What is padding & modes of operation
- Different modes of operation
    - ECB
    - CBC
    - CFB
    - OFB
    - CTR

**Problems:**

- Ciphers are deterministic
- same message + same key = same ciphertext

**Modes of Operation:**

Block Ciphers:

- Block ciphers encrypt fixed size blocks
    - DES encrypts 64-bit blocks with 56-bit key
    - AES encrypts 128-bit blocks with 128/192/256-bit key

Mode of Operation:

- Used to handle arbitrary amounts of data in practise to improve security
- It describes how repeatedly to apply a cipher's single-block operation securely to transform amounts of data larger than a block
- 5 modes defined for AES and DES
- Applicable for block and stream modes

**Message Padding:**

Details:

- One issue that arises with block cipher is how to handle the last block
- Block size fixed: AES-128 bits, DES-64 bits
- Message size input not fixed

Possible Implementation:

- Pad with extra bits at the last block as follows
    - Pad with known non-data values like null
    - Pad with bits + count of pad size
- Overheads
    - Need to recognise padding at the receiving end
    - Must know the count of padding

**Block Cipher Modes of Operation:**

Electronic Code Book (ECB):

- Simplest mode of operation
- Message split into independent blocks
- Each block encrypted independently with the same key
- Each block is substituted with another value, like a code book
- Use in secure transmission of single block of info that needs to be sent
- Session key is then encrypted using master key
- Limitations
    - Deterministic, can be analysed for messages with subtle changes or encrypted twice with the same key to get same ciphertext from same plaintext
    - Message repetitions show in cipher text, obvious in certain types of data and weakness is due to encrypted message blocks being independent

[Chapter%204%20Cipher%20Modes%20cef2bb1f18fb488f88042f66a9ecab83/untitled](Chapter%204%20Cipher%20Modes%20cef2bb1f18fb488f88042f66a9ecab83/untitled)

Cipher Block Chaining (CBC):

- Message split into blocks
- Cipher blocks are linked together
    - Each previous cipher blocks is chained with current plaintext block
    - Initialization Vector (IV) used to start the process
        - A unique binary sequence used for each encryption operation to ensure different ciphertext blocks are generated even if same plaintext block appears multiple time in message
- Used in bulk data encryption, authentication
- Features
    - Ciphertext block depends on all blocks before it, any change to a block affects all following ciphertext blocks
    - Chaining provides an avalanche effect
    - Common IV between sender & receiver
    - IV needs to be random to avoid attackers to brute force attack based on known IV values

[Chapter%204%20Cipher%20Modes%20cef2bb1f18fb488f88042f66a9ecab83/untitled%201](Chapter%204%20Cipher%20Modes%20cef2bb1f18fb488f88042f66a9ecab83/untitled%201)

**Stream Ciphers:**

Details:

- Process message bit-by-bit and uses a pseudo random keystream
- Combined XOR with plaintext bit-by-bit
- Randomness of stream key completely destroys statistically properties in message
- Never reuse stream key or risk recovering messages
- Common stream ciphers
    - RC4
    - Salsa20

[Chapter%204%20Cipher%20Modes%20cef2bb1f18fb488f88042f66a9ecab83/untitled%202](Chapter%204%20Cipher%20Modes%20cef2bb1f18fb488f88042f66a9ecab83/untitled%202)

Properties:

- Design considerations
    - No repetitions over long period
    - Statistically random
    - Depends on large enough key to avoid brute force
- As secure as a block cipher with same size key if properly designed
- Usually simpler and faster as less codes used

**Cipher Feedback (CFB) Mode:**

Details:

- Message stream in bits added to the output of the block cipher
- Each ciphertext block gets 'feedback' into the encryption process in order to encrypt the next plaintext block
- Allows any number of bit to be feedbacked
    - denoted CFB-1, CFB-8 (8 bits), CFB-64 (64 bits, CFB-128 (128 bits)
- Most efficient when all bits in block (64/128) are used
- Used in
    - Stream data encryption
    - Authentication

[Chapter%204%20Cipher%20Modes%20cef2bb1f18fb488f88042f66a9ecab83/untitled%203](Chapter%204%20Cipher%20Modes%20cef2bb1f18fb488f88042f66a9ecab83/untitled%203)

[Chapter%204%20Cipher%20Modes%20cef2bb1f18fb488f88042f66a9ecab83/untitled%204](Chapter%204%20Cipher%20Modes%20cef2bb1f18fb488f88042f66a9ecab83/untitled%204)

Advantages and Limitations:

- Most appropriate when data arrives in bits/bytes (stream mode)
- Limitations
    - Will stall during block encryption after every n-bits if can't keep up with input data as block cipher is used in encryption mode at both ends
    - Errors propagate for several blocks if network transmitting data is "noisy"

**Output Feedback (OFB):**

Details:

- Use unique IV to generate a sequence of output blocks that are XOR with the plaintext
- Output of cipher is added to message stream
- Output is then feedback to the next cycle independent of message
- Used in
    - Stream encryption
    - Noisy channels

[Chapter%204%20Cipher%20Modes%20cef2bb1f18fb488f88042f66a9ecab83/untitled%205](Chapter%204%20Cipher%20Modes%20cef2bb1f18fb488f88042f66a9ecab83/untitled%205)

[Chapter%204%20Cipher%20Modes%20cef2bb1f18fb488f88042f66a9ecab83/untitled%206](Chapter%204%20Cipher%20Modes%20cef2bb1f18fb488f88042f66a9ecab83/untitled%206)

Advantages and Limitations:

- Bit errors do not propagate
    - Single bit error in ciphertext only affect one bit in plaintext, as such, easy for recovery
- Must never reuse the same key+IV
    - If reuse, portion of output stream can be recovered
- Based on research, it is more optimum to use Full Block Feedback (OFB-64 or OFB-128)

[Chapter%204%20Cipher%20Modes%20cef2bb1f18fb488f88042f66a9ecab83/untitled%207](Chapter%204%20Cipher%20Modes%20cef2bb1f18fb488f88042f66a9ecab83/untitled%207)

[Chapter%204%20Cipher%20Modes%20cef2bb1f18fb488f88042f66a9ecab83/untitled%208](Chapter%204%20Cipher%20Modes%20cef2bb1f18fb488f88042f66a9ecab83/untitled%208)

**Counter (CTR):**

Details:

- Similar to OFB but encrypts counter value rather than any feedback value
- Required a different key or a different counter value for every plaintext block
- Used in high-speed network such as ATM encryptions

[Chapter%204%20Cipher%20Modes%20cef2bb1f18fb488f88042f66a9ecab83/untitled%209](Chapter%204%20Cipher%20Modes%20cef2bb1f18fb488f88042f66a9ecab83/untitled%209)

[Chapter%204%20Cipher%20Modes%20cef2bb1f18fb488f88042f66a9ecab83/untitled%2010](Chapter%204%20Cipher%20Modes%20cef2bb1f18fb488f88042f66a9ecab83/untitled%2010)

Advantages and Limitations:

- Efficiency
    - Can do parallel encryptions
    - Block cipher operations can preprocess in advance
    - Good for bursty high speed links
- Provable security
- Breakable if reuse key/counter values

[Chapter%204%20Cipher%20Modes%20cef2bb1f18fb488f88042f66a9ecab83/untitled%2011](Chapter%204%20Cipher%20Modes%20cef2bb1f18fb488f88042f66a9ecab83/untitled%2011)

[Chapter%204%20Cipher%20Modes%20cef2bb1f18fb488f88042f66a9ecab83/untitled%2012](Chapter%204%20Cipher%20Modes%20cef2bb1f18fb488f88042f66a9ecab83/untitled%2012)

[Chapter%204%20Cipher%20Modes%20cef2bb1f18fb488f88042f66a9ecab83/untitled%2013](Chapter%204%20Cipher%20Modes%20cef2bb1f18fb488f88042f66a9ecab83/untitled%2013)
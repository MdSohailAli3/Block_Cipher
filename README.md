# 🔐 Block Cipher Encryption and Decryption (Python)

## 📌 Overview
This project demonstrates a **basic block cipher encryption and decryption system** implemented in Python.  
It converts plaintext into binary, splits it into blocks, applies bitwise operations with a secret key, and
successfully decrypts the data back to the original message.

⚠️ **Disclaimer:** This implementation is **for learning and academic purposes only** and should not be used
for real-world cryptographic security.

---

## 🔑 What is a Block Cipher?
A **block cipher** is a symmetric encryption technique that:
- Encrypts data in **fixed-size blocks**
- Uses the **same secret key** for encryption and decryption
- Relies on **bitwise and logical operations** for data transformation

Block ciphers commonly follow a structure where:
- Data is split into blocks
- A round function modifies one block using a key
- XOR operations combine blocks
- The process is reversible

Examples of real-world block ciphers include **AES** and **DES**.

---

## ⚙️ How a Block Cipher Works (Conceptual Flow)
1. Convert plaintext into binary
2. Split the binary data into two equal halves:
   - Left block (LE)
   - Right block (RE)
3. Generate a secret key
4. Apply a round function on one half using the key
5. XOR the result with the other half
6. Swap the halves (Feistel-style structure)
7. Combine blocks to produce ciphertext
8. Reverse the steps to decrypt the message

This project implements a **multi-round Feistel-like block cipher**.

---

## 🧩 Code Explanation

### 1. Global Variables
```python
KEY = None
LE = None
RE = None
isEncrypted = False
LAYERS_COUNT = 0
```

LE → Left half of the block

RE → Right half of the block

KEY → Secret key (bit array)

isEncrypted → Prevents decryption before encryption

LAYERS_COUNT → Keep track of the current layers

### 2. String to Binary Conversion
```python
string_to_bits_bytearray()
```

Converts input text into a binary string using UTF-8 encoding

Outputs a list of bits (0 and 1)

Required because block ciphers operate on bits

### 3. Block Splitting
```python
LE = bits_array[:len(bits_array)//2]
RE = bits_array[len(bits_array)//2:]
```

Divides the binary data into two equal halves

Mimics real block cipher architecture

### 4. Key Generation
```python
KEY = [(i ^ random_bit) for i in LE]
```

Generates a key using XOR with random bits

Ensures key length matches block size

### 5. Round Function
```python
def func(RE, KEY):
    return RE[i] | KEY[i]
```

Applies bitwise OR (|) between: Right block and Key

Acts as the encryption transformation function

### 6. Encryption Process
```python
newLE = RE
newRE = LE ^ func(RE, KEY)
```

Steps:

Right block becomes the new left block

Left block is XORed with the modified right block

Blocks are concatenated

Binary is converted back to readable text

### 7. Decryption Process
```python
newRE = LE
newLE = RE ^ func(LE, KEY)
```

Reverses the encryption steps

Uses the same key

Works due to the reversible nature of XOR

### 8. Binary to String Conversion
```python
binary_to_string()
```

Groups binary data into 8-bit chunks

Converts them back into characters

### 9. Command-Line Interface

The program provides a menu-driven interface:
```md
1. Encrypt Data
2. Decrypt Data
3. New Message
4. Exit
```

Prevents invalid operations

Allows multiple encrypt/decrypt cycles

## ✅ Key Features

Bit-level encryption

Feistel-style block structure

Symmetric encryption and decryption

Simple CLI interaction

Educational clarity

## ⚠️ Security Notice

This cipher is not secure for real applications due to:

Non-standard key generation

No padding or fixed block size

No cryptographic randomness

## 🚀 Future Enhancements

Secure key scheduling

Padding and block size enforcement

Stronger nonlinear functions

AES-style substitution-permutation layers

## 📄 Conclusion

This project provides a clear and practical demonstration of block cipher fundamentals using Python.
It is ideal for understanding encryption concepts, bitwise operations, and reversible cipher design.

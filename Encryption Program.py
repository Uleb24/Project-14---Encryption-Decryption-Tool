# Project 14 - Encryption Program

import random
import string
import time

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print("Analyzing Message ...")
time.sleep(1)
print("Encrypting ...")
time.sleep(1)
print("Encrypted !")
print(f"Encrypted Message: {cipher_text}")

# DECRYPT
cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print("Analyzing Message ...")
time.sleep(1)
print("Decrypting ...")
time.sleep(1)
print("Decrypted !")
print(f"Decrypted Message: {plain_text}")
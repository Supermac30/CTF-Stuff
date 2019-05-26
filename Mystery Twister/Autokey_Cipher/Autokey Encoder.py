"""
    This script encodes words with the AutoKey Cipher
"""

plaintext = input("input plaintext ")
key = input("input key ")
ciphertext = ""
for i in range(len(plaintext)):
    ciphertext += chr((ord(plaintext[i]) + ord(key[i]))%26 + ord("A"))
    key += plaintext[i]

print("Your encoded String is:",ciphertext)

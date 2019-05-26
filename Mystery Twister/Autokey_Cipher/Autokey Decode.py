"""
    This script decodes words with the AutoKey Cipher
"""

ciphertext = input("input ciphertext ")
key = input("input key ")
plaintext = ""
for i in range(len(ciphertext)):
    plaintext += chr((ord(ciphertext[i]) - ord(key[i]))%26 + ord("A"))
    key += plaintext[i]

print("Your decoded String is:",plaintext)

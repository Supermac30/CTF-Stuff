"""
    This script finds the key when given the ciphertext and plaintext with the AutoKey Cipher
"""

plaintext = input("input plaintext ")
ciphertext = input("input ciphertext ")
key = ""
for i in range(len(plaintext)):
    key += chr((ord(ciphertext[i]) - ord(plaintext[i]))%26 + ord("A"))
for i in range(len(key)):
    if key[i:] == plaintext[:len(key)-i]:
        key = key[:i]
        break

print("The Key is probably:",key)

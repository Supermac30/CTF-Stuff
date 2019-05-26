"""
    This script decodes the ciphertext when knowing
    part of the plaintext with the AutoKey Cipher
"""

ciphertext = input("input ciphertext ")
part = input("input part of plaintext ")

for i in range(len(ciphertext) - len(part)):
    word = ""
    for j in range(len(part)):
        word += chr((ord(ciphertext[i+j]) - ord(part[j]))%26 + ord("A"))
    print("A possible part of the key {} is at position {}".format(word,i))

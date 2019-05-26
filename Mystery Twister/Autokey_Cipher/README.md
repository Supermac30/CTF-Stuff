# Autokey Ciphers
The Autokey cipher is a polyalphabetic substitution cipher characterised by not having a repeated keyword.

To encode the plaintext first concatinate the plaintext to the keyword to make the key, then for i 1...lengthOfPlaintext:

  **_c[i] = K[i] + p[i] % 26_**

The script Autokey Decoder in this directory Automates this.
## Problem Statement
https://www.mysterytwisterc3.org/images/challenges/mtc3-cli-02-autokey-en.pdf

Essentially, the objective is to decode the ciphered text CLWYSXGHAXASPVVHRFQFFDRKMVKOVYY knowing that one of the words in the plaintext is hello.

## Solving The Problem

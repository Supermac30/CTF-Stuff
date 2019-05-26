# Autokey Ciphers
The Autokey cipher is a polyalphabetic substitution cipher characterised by not having a repeated keyword.

To encode the plaintext first concatinate the plaintext to the keyword to make the key, then for i 0...lengthOfPlaintext:

  **_c[i] = K[i] + p[i] % 26_**

I have written scripts above to help make this working with the Autokey cipher easier, Autokey Encoder does the process above automatically
## Problem Statement
https://www.mysterytwisterc3.org/images/challenges/mtc3-cli-02-autokey-en.pdf

Essentially, the objective is to decode the ciphered text CLWYSXGHAXASPVVHRFQFFDRKMVKOVYY knowing that one of the words in the plaintext is WORLD.

## Solving The Problem
Knowing that WORLD is part of the plaintext we can easily find part of the key using:

**_c[i] - p[i] % 26 = K[i]**

By subtracting the plaintext at all positions we should be able to find part of the key.

Running the Autokey Cracking script that checks all positions you'll find lots of what seems like garbage and
```
A possible part of the key WBEKE is at position 11
A possible part of the key THEWO is at position 12
A possible part of the key ZHQGC is at position 13
```

Position 12 looks very promising, especially since it looks like the word WORLD is cut off.
Rerunning the script with THEWORLD as part of the plaintext yields:
```
A possible plaintext HQWWBEKE is at position 8
A possible plaintext ETOTHEWO is at position 9
A possible plaintext HLLZHQGC is at position 10
```

ETOTHEWORLD doesn't make much sence, but it contains our plaintext so will try it anyway. Our objective here is to keep running the script until we find the plaintext that starts at position 0
```
A possible plaintext TNTHQWWBEKE is at position 5
A possible plaintext COMETOTHEWO is at position 6
A possible plaintext DHJHLLZHQGC is at position 7
```

then,
```
A possible plaintext UKGTNTHQWWBEKE is at position 2
A possible plaintext WELCOMETOTHEWO is at position 3
A possible plaintext QJUDHJHLLZHQGC is at position 4
```

add finally,
```
A possible plaintext GHLWELCOMETOTHEWO is at position 0
A possible plaintext PSNQJUDHJHLLZHQGC is at position 1
A possible plaintext AUHVSVWEMZIRZTAUN is at position 2
```

Nice! It looks like our key is GHL. We can be sure of this with the key finder script using WELCOMETOTHEWORLD as our plaintext. Using CLWYSXGHAXASPVVHRFQFFDRKMVKOVYY as the cipher text and GHL as the key in the decoder script results in:
```
input ciphertext CLWYSXGHAXASPVVHRFQFFDRKMVKOVYY
input key GHL
Your decoded String is: WELCOMETOTHEWORLDOFCRYPTOGRAPHY
```

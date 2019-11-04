# mini-rsa
#### Lets decrypt this: [ciphertext](https://2019shell1.picoctf.com/static/8cf588024becf062e35b0e951cefda99/ciphertext)? Something seems a bit small

To encrypt anything in RSA we take the plaintext to the power of e and then modulo n. Since e is so small here and N is so big perhaps m^e is smaller than N.
This means we can take the cube root of the cyphertext. We can do this in [python easily](https://stackoverflow.com/questions/52313392/compute-cube-root-of-extremely-big-number-in-python3/52313476).

Flag: picoCTF{n33d_a_lArg3r_e_db48b19b}

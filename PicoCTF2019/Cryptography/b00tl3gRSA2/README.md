# b00tl3gRSA2
#### In RSA d is alot bigger than e, why dont we use d to encrypt instead of e? Connect with nc 2019shell1.picoctf.com 10814.

d and e are switched in this problem. This means we can decrypt the cyphertext by running `pow(c, 65537, n)` in python.

Flag: picoCTF{bad_1d3a5_4986370}

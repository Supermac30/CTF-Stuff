# asm3
#### What does asm3(0xfe8cf7a4,0xf55018af,0xb8c70926) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](https://2019shell1.picoctf.com/static/e5c2fe7102edd44807fe518ff4063f25/test.S) located in the directory at /problems/asm3_6_22c78ed107ca0b7dd11f868d7203cf8c.

This time the assembly uses smaller registers that are part of larger ones. We can decode this by hand going step by step.

- <+5> : ah = 0xf7, al = 0x00, eax = 0xf700
- <+8> : ah = 0x00, al = 0x00, eax = 0x0000
- <+12>: ah = 0x00, al = 0xe8, eax = 0x00e8
- <+15>: ah = 0x50, al = 0xe8, eax = 0x50e8
- <+18>: ah = 0xe8, al = 0x2f, eax = 0xe82f

Flag: 0xe82f

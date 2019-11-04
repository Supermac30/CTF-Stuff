# Investigative Reversing 1
#### We have recovered a [binary](https://2019shell1.picoctf.com/static/96a72c19db02dd122447a4bfa5faef92/mystery) and a few images: [image](https://2019shell1.picoctf.com/static/96a72c19db02dd122447a4bfa5faef92/mystery.png), [image2](https://2019shell1.picoctf.com/static/96a72c19db02dd122447a4bfa5faef92/mystery2.png), [image3](https://2019shell1.picoctf.com/static/96a72c19db02dd122447a4bfa5faef92/mystery3.png). See what you can make of it. There should be a flag somewhere. Its also found in /problems/investigative-reversing-1_6_34d37d1ca09ecad8586f81060529b1bd on the shell server.

This time the flag is manipulated, divided, and hidden in three different images. When looking into disassembled binary in Ghidra we see that really all it does is break the message up and put a part of it in picture 1 and 3. The script above in this repository solves this problem.

Flag: picoCTF{An0tha_1_8aa498d9}

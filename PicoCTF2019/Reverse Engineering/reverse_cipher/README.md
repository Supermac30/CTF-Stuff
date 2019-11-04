# reverse-cipher
#### We have recovered a [binary](https://2019shell1.picoctf.com/static/e621dd9c2e57f401e6f6fbb6b829ee49/rev) and a [text file](https://2019shell1.picoctf.com/static/e621dd9c2e57f401e6f6fbb6b829ee49/rev_this). Can you reverse the flag. Its also found in /problems/reverse-cipher_0_b784b7d0e499d532eba7269bfdf6a21d on the shell server.

After putting the binary in [Ghidra](https://ghidra-sre.org/) and looking at the disassambled main function we can see exactly what happened to the flag. More specifically we can see that the binary added or subtracted a certain amount to the flag to result in the text in the text file. The script above does the exact opposite to result in the flag.

Flag: picoCTF{r3v3rs39ba4806b}

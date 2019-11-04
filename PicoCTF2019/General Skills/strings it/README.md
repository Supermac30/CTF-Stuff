# strings it
#### Can you find the flag in file without running it? You can also find the [file](https://2019shell1.picoctf.com/static/e010adf66e96d25d0efe739434b6e801/strings) in /problems/strings-it_4_e276260a1b64a734b4178a280d25b754 on the shell server.

Running the strings command on the file and looking for the output with picoctf in it with grep finds the flag for us
```
Supermac30@pico-2019-shell1:/problems/strings-it_4_e276260a1b64a734b4178a280d25b754$ strings strings | grep picoCTF
picoCTF{5tRIng5_1T_c611cac7}
```

Flag: picoCTF{5tRIng5_1T_c611cac7}

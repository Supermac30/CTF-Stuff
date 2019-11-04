# First Grep: Part II
#### Can you find the flag in /problems/first-grep--part-ii_5_956980126dc47c50540b0f8f35a8e443/files on the shell server? Remember to use grep.

Using the grep -r command we can find the flag

```
Supermac30@pico-2019-shell1:/problems/first-grep--part-ii_5_956980126dc47c50540b0f8f35a8e443$ grep -r "picoCTF" files
files/files6/file23:picoCTF{grep_r_to_find_this_0898e9c9}
```

Flag: picoCTF{grep_r_to_find_this_0898e9c9}

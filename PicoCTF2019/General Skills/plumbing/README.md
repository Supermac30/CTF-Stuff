# plumbing
#### Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to 2019shell1.picoctf.com 9525.

Piping the output to grep to search for the flag is the easiest way to solve this problem.
```
supermac30@LAPTOP-D0Q1SN5H:~$ nc 2019shell1.picoctf.com 9525 | grep picoCTF
picoCTF{digital_plumb3r_dd86d037}
```

Flag: picoCTF{digital_plumb3r_dd86d037}

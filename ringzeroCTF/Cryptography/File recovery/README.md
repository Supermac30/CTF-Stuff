# File recovery

To solve this challenge all we need to do is use openssl
```
supermac30@LAPTOP-D0Q1SN5H:~/ctfstuff/ringzero$ openssl rsautl -decrypt -in flag.enc -out flag.txt -inkey private.pem
supermac30@LAPTOP-D0Q1SN5H:~/ctfstuff/ringzero$ cat flag.txt
FLAG-vOAM5ZcReMNzJqOfxLauakHx
```

Flag: FLAG-vOAM5ZcReMNzJqOfxLauakHx
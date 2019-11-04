"""
    This script uses the pwn library's process function to run the program, read the output, pass it through eval and input the answer.
"""
from pwn import *
p = process('/problems/time-s-up_1_7d4f79c3df3e1b044801573eea5722be/times-up')
out = p.recvline()
answer = eval(out[10:])
p.sendline(str(answer))
flag = p.recvall()
print(flag)

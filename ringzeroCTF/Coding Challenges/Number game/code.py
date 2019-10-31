# Written in python2
from pwn import *
shell = ssh(host='challenges.ringzer0team.com', port=10130, user='number', password='Z7IwIMRC2dc764L')
sh = shell.run('sh')
out = ""
for i in range(4):
        out = sh.recvline()
MAX = 10000
MIN = 0
guess = 5000
sh.sendline(str(guess))
out = sh.recvline()
out = sh.recvline()
for i in range(11):
        while "small" in out or "big" in out:
                if "small" in out:
                        MIN = guess
                elif "big" in out:
                        MAX = guess
                guess = (MIN+MAX)//2
                sh.sendline(str(guess))
                out = sh.recvline()
                out = sh.recvline()
        print "|"+out[:-1]+"|"
        MAX = 10000
        MIN = 0
        guess = 5000
        sh.sendline(str(guess))
        out = sh.recvline()
        out = sh.recvline()
sh.interactive()
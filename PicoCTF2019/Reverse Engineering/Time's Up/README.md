# Time's Up
#### Time waits for no one. Can you solve this before time runs out? [times-up](https://2019shell1.picoctf.com/static/e16f7e84ccd54f27fa239c736247b500/times-up), located in the directory at /problems/time-s-up_1_7d4f79c3df3e1b044801573eea5722be.

We can automate this using the [pwn library](http://docs.pwntools.com/en/stable/tubes/processes.html) and the [eval function](https://docs.python.org/3/library/functions.html#eval). Using the script above we can automate the process to answer the program's question fast enough.
The script has to be run in the same directory as the flag.txt flag in order for it to be read.
```
Supermac30@pico-2019-shell1:/problems/time-s-up_1_7d4f79c3df3e1b044801573eea5722be$ python ~/automate.py
[+] Starting local process '/problems/time-s-up_1_7d4f79c3df3e1b044801573eea5722be/times-up': pid 2794321
[+] Receiving all data: Done (104B)
[*] Process '/problems/time-s-up_1_7d4f79c3df3e1b044801573eea5722be/times-up' stopped with exit code 0 (pid 2794321)
Setting alarm...
Solution? Congrats! Here is the flag!
picoCTF{Gotta go fast. Gotta go FAST. #3daa579a}
```
Flag: picoCTF{Gotta go fast. Gotta go FAST. #3daa579a}

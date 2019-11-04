# Need For Speed
#### The name of the game is [speed](https://www.youtube.com/watch?v=8piqd2BWeGI). Are you quick enough to solve this problem and keep it above 50 mph? [need-for-speed](https://2019shell1.picoctf.com/static/0087e4830ca81141d6fa4a8b4a9767ba/need-for-speed).

Disassembling the binary with gdb we see that the code sets a timer before printing the flag.
```
(gdb) disass main
Dump of assembler code for function main:
   0x0000000000000974 <+0>:     push   %rbp
   0x0000000000000975 <+1>:     mov    %rsp,%rbp
   0x0000000000000978 <+4>:     sub    $0x10,%rsp
   0x000000000000097c <+8>:     mov    %edi,-0x4(%rbp)
   0x000000000000097f <+11>:    mov    %rsi,-0x10(%rbp)
   0x0000000000000983 <+15>:    mov    $0x0,%eax
   0x0000000000000988 <+20>:    callq  0x932 <header>
   0x000000000000098d <+25>:    mov    $0x0,%eax
   0x0000000000000992 <+30>:    callq  0x87f <set_timer>
   0x0000000000000997 <+35>:    mov    $0x0,%eax
   0x000000000000099c <+40>:    callq  0x8d7 <get_key>
   0x00000000000009a1 <+45>:    mov    $0x0,%eax
   0x00000000000009a6 <+50>:    callq  0x906 <print_flag>
   0x00000000000009ab <+55>:    mov    $0x0,%eax
   0x00000000000009b0 <+60>:    leaveq
   0x00000000000009b1 <+61>:    retq
End of assembler dump.
```
Luckily we can use gdb to jump to where ever we need to with the jump function. First we need to set a break point when set_timer starts then reach it during execution.
```
(gdb) b set_timer
Breakpoint 1 at 0x883
(gdb) run
Starting program: /home/supermac30/picoctf2019/need_for_speed/need-for-speed
Keep this thing over 50 mph!
============================


Breakpoint 1, 0x0000000008000883 in set_timer ()
```
Then we can jump to the get_key function to calculate the key without the timer being set. We can use CTRL-C to pause execution once the key is calculated.
```
(gdb) jump get_key
Continuing at 0x80008db.
Creating key...
Finished
Creating key...
^C
Program received signal SIGINT, Interrupt.
0x000000000800084c in calculate_key ()
```
Then all we have to do is to jump to the print_flag function to get the flag.
```
(gdb) jump print_flag
Continuing at 0x800090a.
Printing flag:
PICOCTF{Good job keeping bus #236cb1c9 speeding along!}
Finished
Printing flag:
hI{OzT|{}oTdjSbk[eNiQg`b5sa#p3tc!1'9ds5e#d/n  )l'n.!7
[Inferior 1 (process 51) exited normally]
```
Flag: PICOCTF{Good job keeping bus #236cb1c9 speeding along!}

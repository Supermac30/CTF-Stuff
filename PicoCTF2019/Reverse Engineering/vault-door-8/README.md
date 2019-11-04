# vault-door-8
#### Apparently Dr. Evil's minions knew that our agency was making copies of their source code, because they intentionally sabotaged this source code in order to make it harder for our agents to analyze and crack into! The result is a quite mess, but I trust that my best special agent will find a way to solve it. The source code for this vault is here: [VaultDoor8.java](https://2019shell1.picoctf.com/static/f2fc1401192dfbbcf8d7eeb378671986/VaultDoor8.java)

The first step to solving this problem is to make the code readable. We can do this in a [beautifier](https://codebeautify.org/javaviewer).
We then see that the code shifts the bits of each character in the password. Doing this in reverse results in the flag. The script above does just that.

Flag: picoCTF{s0m3_m0r3_b1t_sh1fTiNg_1169cac67}

# vault-door-4
#### This vault uses ASCII encoding for the password. The source code for this vault is here: [VaultDoor4.java](https://2019shell1.picoctf.com/static/6e7e8c58349540f3723d43165a6c9b45/VaultDoor4.java)

Converting the first 8 bytes from decimal to ascii, the second eight bytes from hex to ascii, the third eight bytes from octal to ascii, then concatinating all of them with
together and with the last eight bytes results in the flag.

Flag: picoCTF{jU5t_4_bUnCh_0f_bYt3s_b9e92f76ac}

# vault-door-1
#### This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: [VaultDoor1.java](https://2019shell1.picoctf.com/static/7c285a3b805b4294bf9d67fa2cb7e2d0/VaultDoor1.java)

Looking through the source code we can find the function checkPassword. 
This function verifies the authenticity of the password by checking the value at each index.
```
public boolean checkPassword(String password) {
        return password.length() == 32 &&
               password.charAt(0)  == 'd' &&
               password.charAt(29) == '7' &&
               password.charAt(4)  == 'r' &&
               password.charAt(2)  == '5' &&
               password.charAt(23) == 'r' &&
               password.charAt(3)  == 'c' &&
               password.charAt(17) == '4' &&
               password.charAt(1)  == '3' &&
               password.charAt(7)  == 'b' &&
               password.charAt(10) == '_' &&
               password.charAt(5)  == '4' &&
               password.charAt(9)  == '3' &&
               password.charAt(11) == 't' &&
               password.charAt(15) == 'c' &&
               password.charAt(8)  == 'l' &&
               password.charAt(12) == 'H' &&
               password.charAt(20) == 'c' &&
               password.charAt(14) == '_' &&
               password.charAt(6)  == 'm' &&
               password.charAt(24) == '5' &&
               password.charAt(18) == 'r' &&
               password.charAt(13) == '3' &&
               password.charAt(19) == '4' &&
               password.charAt(21) == 'T' &&
               password.charAt(16) == 'H' &&
               password.charAt(27) == '3' &&
               password.charAt(30) == 'a' &&
               password.charAt(25) == '_' &&
               password.charAt(22) == '3' &&
               password.charAt(28) == 'b' &&
               password.charAt(26) == '0' &&
               password.charAt(31) == '0';
}
```
Reversing this by hand is a bit tedious so I wrote a script that automates it. By putting the function in a text editor and replacing '.charAt' with '[', '&&' with '', and ')' with ']'
you get the script above. Running it results in the password.

Flag: picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_03b7a0}

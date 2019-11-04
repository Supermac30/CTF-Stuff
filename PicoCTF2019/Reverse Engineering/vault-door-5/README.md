# vault-door-5
#### In the last challenge, you mastered octal (base 8), decimal (base 10), and hexadecimal (base 16) numbers, but this vault door uses a different change of base as well as URL encoding! The source code for this vault is here: [VaultDoor5.java](https://2019shell1.picoctf.com/static/7f424ab1835c1d5f94e3a3d35c79c141/VaultDoor5.java)

To solve this challenge all we have to do is to convert the string contained in the function checkPassword from [base64 to text](https://www.base64decode.org/), then the text from [url encoding to the flag](https://meyerweb.com/eric/tools/dencoder/).

Flag: picoCTF{c0nv3rt1ng_fr0m_ba5e_64_0f309d40}

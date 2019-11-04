# Easy1
#### The one time pad can be cryptographically secure, but not when you know the key. Can you solve this? We've given you the encrypted flag, key, and a table to help UFJKXQZQUNB with the key of SOLVECRYPTO. Can you use this [table](https://2019shell1.picoctf.com/static/30d4405c34cf6490b082e6cf8f56ac56/table.txt) to solve it?.

This is an example of a vigenere cipher. Each letter is added to the corresponding letter in the key according to the table.
We can decode this manually using the table, or using an [online decoder](https://www.dcode.fr/vigenere-cipher)

Flag: picoCTF{CRYPTOISFUN}

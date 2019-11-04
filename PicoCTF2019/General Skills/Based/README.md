# Based
#### To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. Can you get the flag from this program to prove you are on the way to becoming 1337? Connect with nc 2019shell1.picoctf.com 29594.

When connecting we get three questions asking to convert binary, octal, and hexadecimal to ascii. We can use online tools to do this quickly

https://www.rapidtables.com/convert/number/binary-to-ascii.html

http://www.unit-conversion.info/texttools/octal/

https://www.rapidtables.com/convert/number/hex-to-ascii.html

```
supermac30@LAPTOP-D0Q1SN5H:~$ nc 2019shell1.picoctf.com 29594
Let us see how data is stored
lime
Please give the 01101100 01101001 01101101 01100101 as a word.
...
you have 45 seconds.....

Input:
lime
Please give me the  163 157 143 153 145 164 as a word.
Input:
socket
Please give me the 736f636b6574 as a word.
Input:
socket
You've beaten the challenge
Flag: picoCTF{learning_about_converting_values_e67b1990}
```

Flag: picoCTF{learning_about_converting_values_e67b1990}

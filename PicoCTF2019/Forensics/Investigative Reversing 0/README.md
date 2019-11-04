# Investigative Reversing 0
#### We have recovered a [binary](https://2019shell1.picoctf.com/static/6c499ab246595090d699b87b99570275/mystery) and an [image](https://2019shell1.picoctf.com/static/6c499ab246595090d699b87b99570275/mystery.png). See what you can make of it. There should be a flag somewhere. Its also found in /problems/investigative-reversing-0_0_ebc669df876196bdc09a2f54fd5fffed on the shell server.

Looking at the binary in Gihdra we can see that it reads the flag file and appends a manipulated version of it in the image. Looking at the image's hexdump we can see the text 'picoCTK€k5zsid6q_fb69f6c2}' after the IEND chunk. Doing what the binary does in reverse results in the flag. The code above does just that.

Flag: picoCTF{f0und_1t_fb69f6c2}

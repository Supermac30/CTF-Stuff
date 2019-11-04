# WhitePages
#### I stopped using YellowPages and moved onto WhitePages... but [the page they gave me](https://2019shell1.picoctf.com/static/48e43341bf6703355b331b07d05eee8d/whitepages.txt) is all blank!

Looking in the file we see a lot of white space but also two characters, 0x20 and 0x2003. Changing all the 0x20s to 1s and all the 0x2003 
to 0s then converting the binary to ascii results in the flag.

Flag: picoCTF{not_all_spaces_are_created_equal_f006c045f6b402ce4bc749dc7a262380}

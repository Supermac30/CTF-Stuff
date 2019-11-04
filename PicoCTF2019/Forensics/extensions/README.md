# extensions
#### This is a really weird text file [TXT](https://2019shell1.picoctf.com/static/45886ed4b6d5d1dc74c4944fcf4b4041/flag.txt)? Can you find the flag?

This txt file looks like its filled with garbage when opened. The first line of the text file has the word PNG in it, this is because of 
the PNG's file header which means that the '.txt' extention is incorrect. Replacing it with '.png' results in the flag.

Flag: picoCTF{now_you_know_about_extensions}

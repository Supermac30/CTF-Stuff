# 1_wanna_b3_a_r0ck5tar
#### I wrote you another [song](https://2019shell1.picoctf.com/static/0690cdfc040e177175b2822f690ec4e0/lyrics.txt). Put the flag in the picoCTF{} flag format

This time when running the code in the online interpreter we are asked for input and do not receive any output. To bypass this we can use a [transpiler from Rockstar to python](https://pypi.org/project/rockstar-py/).
Running the transpiler we get can see a series of variable assignements when converted to ascii read BONJOVI.

Flag: picoCTF{BONJOVI}

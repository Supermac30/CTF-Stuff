# m00nwalk2
#### Revisit the last [transmission](https://2019shell1.picoctf.com/static/1b9456ca6c4ee2a2aa094d98581f8c37/message.wav). We think this transmission contains a hidden message. There are also some clues [clue 1](https://2019shell1.picoctf.com/static/1b9456ca6c4ee2a2aa094d98581f8c37/clue1.wav), [clue 2](https://2019shell1.picoctf.com/static/1b9456ca6c4ee2a2aa094d98581f8c37/clue2.wav), [clue 3](https://2019shell1.picoctf.com/static/1b9456ca6c4ee2a2aa094d98581f8c37/clue3.wav). You can also find the files in /problems/m00nwalk2_0_c513cbf9ae6c76876372b8e29826e77b.

We can do the exact same thing [as last time](https://github.com/Supermac30/PicoCTF-2019/tree/master/Forensics/m00nwalk) to decode these SSTV transmissions. [This tutorial](https://ourcodeworld.com/articles/read/956/how-to-convert-decode-a-slow-scan-television-transmissions-sstv-audio-file-to-images-using-qsstv-in-ubuntu-18-04) is, again, very helpful.

This time we get a password, hidden_stegosaurus, and a name, Alan Eliasen Future boy. Going to https://futureboy.us/stegano/decinput.html and inputting the wav file transmitted with the password results in the flag.

Flag: picoCTF{the_answer_lies_hidden_in_plain_sight}

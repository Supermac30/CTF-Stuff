# Glory of the Garden
#### This [garden](https://2019shell1.picoctf.com/static/38b5c0bde1a6a92d282b128c71799722/garden.jpg) contains more than it seems. You can also find the file in /problems/glory-of-the-garden_4_cf9f4aaf458caf5268f8cf0a6465eb98 on the shell server.

Searching through the hex dump of the file we can find the flag hidden at the bottom
```
Supermac30@pico-2019-shell1:/problems/glory-of-the-garden_4_cf9f4aaf458caf5268f8cf0a6465eb98$ xxd garden.jpg
00000000: ffd8 ffe0 0010 4a46 4946 0001 0101 0048  ......JFIF.....H
00000010: 0048 0000 ffe2 0c58 4943 435f 5052 4f46  .H.....XICC_PROF
00000020: 494c 4500 0101 0000 0c48 4c69 6e6f 0210  ILE......HLino..
...
00230550: a2bb bdac 9687 98e4 d3b2 e87f ffd9 4865  ..............He
00230560: 7265 2069 7320 6120 666c 6167 2022 7069  re is a flag "pi
00230570: 636f 4354 467b 6d6f 7265 5f74 6861 6e5f  coCTF{more_than_
00230580: 6d33 3374 735f 7468 655f 3379 3336 4243  m33ts_the_3y36BC
00230590: 4136 3834 447d 220a                      A684D}".
```
Flag: picoCTF{more_than_m33ts_the_3y36BCA684D}

# So Meta
#### Find the flag in this [picture](https://2019shell1.picoctf.com/static/61e816c3ab6abee2bda49f438bd49571/pico_img.png). You can also find the file in /problems/so-meta_3_6dc950904c3ee41f324ae8d9f142f2b8.

The Metadata of a png can be found in the tEXt chunk in its hexdump. Looking for tEXt in the hexdump of the file shows us that the artist is the flag. We can see this in the tEXt chunk at the bottom of the file.
```
Supermac30@pico-2019-shell1:/problems/so-meta_3_6dc950904c3ee41f324ae8d9f142f2b8$ xxd pico_img.png | more
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
00000010: 0000 0258 0000 0258 0802 0000 0031 040f  ...X...X.....1..
00000020: 8b00 0000 1974 4558 7453 6f66 7477 6172  .....tEXtSoftwar
00000030: 6500 4164 6f62 6520 496d 6167 6552 6561  e.Adobe ImageRea
00000040: 6479 71c9 653c 0000 0322 6954 5874 584d  dyq.e<..."iTXtXM
...
0001a8a0: 288a 2208 298a a228 8a20 a428 8aa2 2882  (.".)..(. .(..(.
0001a8b0: 90a2 288a a232 41ff 1760 001d 887a 0149  ..(..2A..`...z.I
0001a8c0: 576c 1700 0000 2074 4558 7441 7274 6973  Wl.... tEXtArtis
0001a8d0: 7400 7069 636f 4354 467b 7330 5f6d 3374  t.picoCTF{s0_m3t
0001a8e0: 615f 3433 6632 3533 6262 7d00 2025 5200  a_43f253bb}. %R.
0001a8f0: 0000 0049 454e 44ae 4260 82              ...IEND.B`.
```

The challenge can also be solved using [an online tool](http://exif.regex.info/exif.cgi).

Flag: picoCTF{s0_m3ta_43f253bb}

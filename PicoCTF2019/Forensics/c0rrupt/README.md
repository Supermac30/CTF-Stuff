# c0rrupt
#### We found this [file](https://2019shell1.picoctf.com/static/3435d990f1d20fe3563cbb897b4c96db/mystery). Recover the flag. You can also find the file in /problems/c0rrupt_0_1fcad1344c25a122a00721e4af86de13.

This was is my favourite problem in this ctf despite not being worth much points. To solve this problem we must first find out what type of file it is.
We can do this by looking at the first 8 bytes, the [file signature](https://en.wikipedia.org/wiki/List_of_file_signatures). After opening the hexdump
with fhred on windows or hexedit on linux we see that the first 8 bytes are `89 65 4e 34 0d 0a b0 aa` this is very close to a png's file signature, `89 50 4E 47 0D 0A 1A 0A`. 

Changing the file signature doesn't completely fix the png. We have to look at the chunks individually. A png file is made up of different chunks
which are listed on the [png specification](https://www.w3.org/TR/2003/REC-PNG-20031110/#11Chunks). Looking at the chunks we see that after the header
there must exist a IHDR chunk. Changing the `43 22 44 52` bytes to `49 48 44 52` fixes it. The file is still broken, however.

Looking through the hex dump we don't see any mistakes up until the pHYs chunk. This chunk encodes the pixels per unit on both the x and y axis. Strangely the
pixels per unit on the x-axis is `aa 00 16 25` and `00 00 16 25` on the y-axis. Removing the first aa on the x-axis makes both of them the same and fixes the unreasonably
large pixels per unit on the x-axis. This still doesn't fix our png completely.

There is a strange chunk with a massive length right after the pHYs chunk. After some inspection it should be clear that it is an IDAT chunk.
Changing the bytes from `ab 44 45 54` to `49 44 41 54` results in a fixed png.

Flag: picoCTF{c0rrupt10n_1847995}

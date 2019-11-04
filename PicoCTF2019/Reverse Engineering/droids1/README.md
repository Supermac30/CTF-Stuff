# droids1
#### Find the pass, get the flag. Check out this [file](https://2019shell1.picoctf.com/static/6bf44e4070f1d2173e72a28e77f0d086/one.apk). You can also find the file in /problems/droids1_0_b7f94e21c7e45e6604972f9bc3f50e24.

Running the apk this time it seems as if we need a password. To find the password we have to disassemble the apk file. We can do this with apktools and th command `apktool d one.apk`.
Performing a search in the res folder for a password gives us:
```
supermac30@LAPTOP-D0Q1SN5H:~/picoctf2019/one$ grep -r password res
res/values/public.xml:    <public type="string" name="password" id="0x7f0b002f" />
res/values/strings.xml:    <string name="password">opossum</string>
```
This reveals the password 'opossum' and allows us to get the flag.

Flag: picoCTF{pining.for.the.fjords}

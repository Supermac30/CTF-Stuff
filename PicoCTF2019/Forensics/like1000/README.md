# like1000
#### This [.tar file](https://2019shell1.picoctf.com/static/8694f84879d3b7c0dcf775930f4665fc/1000.tar) got tarred alot. Also available at /problems/like1000_0_369bbdba2af17750ddf10cc415672f1c.

This is a simple scripting problem. Running the command below in the same directory as the tar file results in a png containing the flag.
```
for i in {1000..1}; do tar -xvf $i.tar; rm $i.tar; done
```
Flag: picoCTF{l0t5_0f_TAR5}

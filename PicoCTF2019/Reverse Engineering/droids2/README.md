# droids2
#### Find the pass, get the flag. Check out this [file](https://2019shell1.picoctf.com/static/5357598f1a403425fc76f17764014e59/two.apk). You can also find the file in /problems/droids2_0_bf474794b5a228db3498ba3198db54d7.

This time the password is not hidden in the res file. Looking in the smali folder we find some interesting code in the file 'FlagstaffHill.smali'.
Looking inside we see code that adds values to an array and spits them out in a certain order. [This](http://androidcracking.blogspot.com/2011/01/example-structuressmali.html) and [this](http://pallergabor.uw.hu/androidblog/dalvik_opcodes.html) were extremely helpful when decoding the assembly.
The script above does exactly what the assembly does to find the password. Running it reveals the password:
```
dismass.ogg.weatherwax.aching.nitt.garlick
```
Putting this in results in the flag.

Flag: picoCTF{what.is.your.favourite.colour}

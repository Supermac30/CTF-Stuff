# First Grep
#### Can you find the flag in [file](https://2019shell1.picoctf.com/static/3f6065eec2d3ed644932ada577a74334/file)? This would be really tedious to look through manually, something tells me there is a better way. You can also find the file in /problems/first-grep_0_93be1631acf1a93b98cdcc3e7b9fdc52 on the shell server.

Using the grep command we can find the flag hidden in the data.
```
Supermac30@pico-2019-shell1:/problems/first-grep_0_93be1631acf1a93b98cdcc3e7b9fdc52$ cat file | grep picoCTF
picoCTF{grep_is_good_to_find_things_4b2451ea}
```

Flag: picoCTF{grep_is_good_to_find_things_4b2451ea}

# Beginners
This file contains my solutions for the beginner challenges in Houseplant CTF

## Beginner 1
We are given a base64 encoded flag to decode. We can do this in python.
```
>>> import base64
>>> base64.b64decode("cnRjcHt5b3VyZV92ZXJ5X3dlbGNvbWV9")
b'rtcp{youre_very_welcome}'
```
Flag: rtcp{youre_very_welcome}

## Beginner 2
This time we are given a hex encoded string.
```
>>> encoded = "72 74 63 70 7b 62 6f 62 5f 79 6f 75 5f 73 75 63 6b 5f 61 74 5f 62 65 69 6e 67 5f 65 6e 63 6f 75 72 61 67 69 6e 67 7d".split()
>>> flag = ""
>>> for character in encoded:
	flag += chr(int(character, 16))

>>> flag
'rtcp{bob_you_suck_at_being_encouraging}'
```
Flag: rtcp{bob_you_suck_at_being_encouraging}

## Beginner 3
And this time we're given an octal encoded string.
```
>>> encoded = "162 164 143 160 173 163 165 145 137 155 145 137 151 137 144 151 144 156 164 137 153 156 157 167 137 167 150 141 164 137 157 143 164 141 154 137 167 141 163 137 157 153 141 171 77 41 175".split()
>>> flag = ""
>>> for character in encoded:
	flag += chr(int(character, 8))

>>> flag
'rtcp{sue_me_i_didnt_know_what_octal_was_okay?!}'
```
Flag: rtcp{sue_me_i_didnt_know_what_octal_was_okay?!}

## Beginner 3
The flag is now encrypted with a basic caeser cipher. We can find the shift amount by looking at the distance between the first letter in the ciphertext, 'e' and the first letter in the flag, 'r'. A simple python script does the rest.
```
def caeser(word, amount):
    plaintext = ""
    for character in word:
        if not (ord("a") <= ord(character) and ord(character) <= ord("z")):
            plaintext += character
            continue
        plaintext += chr(((ord(character) - ord("a") + amount) % 26) + ord("a"))
    return plaintext

print(caeser("egpc{lnyy_orggre_cnegvpvcngr}", ord("r")-ord("e")))
```
Flag: rtcp{yall_better_participate}

## Beginner 5
We can use an [online morse decoder](https://convertcase.net/morse-code-translator/) to get the flag.
Flag: rtcp{many_beeps_and_boops}

## Beginner 6
Here the flag is encoded in an encoder that encodes a as 1, ba as 2, and so on.
```
>>> ciphertext = "26 26 26 26 26 26 26 26 19 12 5 5 16 9 14 7 9 14 16 8 25 19 9 3 19".split()
>>> plaintext = ""
>>> for character in ciphertext:
	plaintext += chr(ord("a") + int(character) - 1)

>>> plaintext
'zzzzzzzzsleepinginphysics'
```
Flag: rtcp{zzzzzzzzsleepinginphysics}

## Beginner 7
The flag is encoded with an atbash cipher.
```
>>> ciphertext = "igxk{fmovhh_gsvb_ziv_nvzm}"
>>> plaintext = ""
>>> for character in ciphertext:
	if not (ord("a") <= ord(character) and ord(character) <= ord("z")):
		plaintext += character
		continue
	plaintext += chr(25 + 2 * ord("a") - ord(character))

	
>>> plaintext
'rtcp{unless_they_are_mean}'
```
Flag: rtcp{unless_they_are_mean}

## Beginner 8
This time the cipher used in beginner 6 is used again, but is encoded in binary first.
```
>>> ciphertext = "00110 01110 00100 00000 10011 00101 01110 01110 00011 00011 01110 01101 10011 10010 10011 00000 10001 10101 00100".split()
>>> plaintext = ""
>>> for character in ciphertext:
	plaintext += chr(ord("a") + int(character, 2))

	
>>> plaintext
'goeatfooddontstarve'
```
Flag: rtcp{goeatfooddontstarve}

## Beginner 9
In the final challenge we combine everything so far. We can do this easily using cyberchef. Using [this](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)From_Hex('Auto')From_Morse_Code('Space','Line%20feed')From_Binary('Space')A1Z26_Cipher_Decode('Space')Atbash_Cipher()ROT13(true,true,13)) and adding the ciphertext in the input should result in the flag.

Flag: rtcp{nineornone}
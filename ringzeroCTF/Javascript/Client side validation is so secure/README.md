# Client side validation is so secure

To solve this challenge we have to get through a simple user login with frontside js authentication. The key to solving this puzzle is through this line
```
if(u == "admin" && p == String.fromCharCode(74,97,118,97,83,99,114,105,112,116,73,115,83,101,99,117,114,101)) {
```
Setting the user to admin and the password to the decimal converted to ascii, JavaScriptIsSecure, we get the flag.

Flag: FLAG-66Jq5u688he0y46564481WRh
# Most Secure Crypto Algo

Looking at the source we can see that user is encoded in bytes, `u == "\x68\x34\x78\x30\x72"`, which in ascii is `h4x0r`. 

The password is checked using AES. Luckily, we are given the key and the iv. They are both manipulations on some SHA256 hashed string. We can easily decode this using the console and running the following lines of code:
```
var k = CryptoJS.SHA256("\x93\x39\x02\x49\x83\x02\x82\xf3\x23\xf8\xd3\x13\x37");
var p = CryptoJS.AES.decrypt("ob1xQz5ms9hRkPTx+ZHbVg==", CryptoJS.enc.Hex.parse(k.toString().substring(0,32)), { iv: CryptoJS.enc.Hex.parse(k.toString().substring(32,64)) }).toString();
console.log(p);
```
Turning the password from hex to ascii we get a password of `PassW0RD!289%!*`

Flag: FLAG-gYtLBa66178DG7l28Uu5lW45CR

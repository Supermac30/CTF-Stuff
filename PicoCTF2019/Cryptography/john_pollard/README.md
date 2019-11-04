# john_pollard
#### Sometimes RSA [certificates](https://2019shell1.picoctf.com/static/ccd7ba84ead965bd2033a54c4dbb8ae0/cert) are breakable

When running the certificate through [an online decoder](https://www.sslchecker.com/certdecoder) we get the modulus to be 4966306421059967.
We can then factor it using [this online tool](https://www.alpertron.com.ar/ECM.HTM) to get the flag.

Flag: picoCTF{73176001,67867967}

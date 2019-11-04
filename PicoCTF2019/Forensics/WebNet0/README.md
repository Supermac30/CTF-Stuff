# WebNet0
#### We found this [packet capture](https://2019shell1.picoctf.com/static/470e17b168561f9eabdfa95e412dbe10/capture.pcap) and [key](https://2019shell1.picoctf.com/static/470e17b168561f9eabdfa95e412dbe10/picopico.key). Recover the flag. You can also find the file in /problems/webnet0_0_363c0e92cf19b68e5b5c14efb37ed786.

Opening the packet file we see a lot of garbage. We also see encrypted messages sent with the TLS protocol. In wireshark going into Edit then preferences on the top tool bar
then expanding the protocols menu we can see a tls section. In there going into rsa keys and adding the key in the challenge description decrypts the messages. We can simply
press CTRL-F and search for picoCTF in the packet details to find the flag. 


Flag: picoCTF{nongshim.shrimp.crackers}

# WebNet1
#### We found this [packet capture](https://2019shell1.picoctf.com/static/62437b61d31d915b837cce3396c204d9/capture.pcap) and [key](https://2019shell1.picoctf.com/static/62437b61d31d915b837cce3396c204d9/picopico.key). Recover the flag. You can also find the file in /problems/webnet1_0_d63b267c607b8fedbae100068e010422.

We can solve this problem in almost exactly the same way we solved [WebNet0](https://github.com/Supermac30/PicoCTF-2019/tree/master/Forensics/WebNet0). This time the flag won't come up when searching through the packet's details. Looking through the reassembled SSL would reveal the flag.

Flag: picoCTF{honey.roasted.peanuts}

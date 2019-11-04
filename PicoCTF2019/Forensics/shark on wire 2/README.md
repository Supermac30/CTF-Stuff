# shark on wire 2
#### We found this [packet capture](https://2019shell1.picoctf.com/static/dcd259894e0efe9d6e91da2af47e6369/capture.pcap). Recover the flag that was pilfered from the network. You can also find the file in /problems/shark-on-wire-2_0_3e92bfbdb2f6d0e25b8d019453fdbf07.

Looking at the packet in wireshark we can see a lot of garbage but also a packet containing the word 'start' and another containing the word 'end'. 
Upon further inspection we can see suspicious packets being sent from 10.0.0.66 to 10.0.0.1 from different ports. Joining together the port numbers, without the beginning 5 results results in the list of numbers below. Converting this to ascii results in the flag.

```
112 105 99 111 67 84 70 123 112 49 76 76 102 51 114 51 100 95 100 97 116 97 95 118 49 97 95 115 116 51 103 48 125
```

Flag: picoCTF{p1LLf3r3d_data_v1a_st3g0}

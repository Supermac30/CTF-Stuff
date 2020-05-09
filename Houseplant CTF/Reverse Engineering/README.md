# Reverse Engineering
## Fragile
Looking at the source we only need to subtract the two strings line by line to find the flag.
```
>>> total = "ÐdØÓ§åÍaèÒÁ¡"
>>> flag = "h1_th3r3_1ts_m3"
>>> the_flag = ""
>>> for i in range(len(flag)):
	the_flag += chr(ord(total[i])-ord(flag[i]))

	
>>> the_flag
'h3y_1ts_n0t_b4d'
```
Flag: rtcp{h3y_1ts_n0t_b4d}

## Breakable

Flag: rtcp{0mg_1m_s0_pr0ud_}

## Squeezy
```
>>> the_flag = "1m_s0_pr0ud_2o"
>>> result = "HxEMBxUAURg6I0QILT4UVRolMQFRHzokRBcmAygNXhkqWBw="
>>> import base64
>>> result = base64.b64decode(result)
>>> result
b'\x1f\x11\x0c\x07\x15\x00Q\x18:#D\x08->\x14U\x1a%1\x01Q\x1f:$D\x17&\x03(\r^\x19*X\x1c'
>>> key = "meownyameownyameownyameownyameownya"
>>> ''.join(chr(a ^ ord(b)) for a,b in zip(result, key))
'rtcp{y0u_L3fT_y0uR_x0r_K3y_bEh1nD!}'
>>> 
```

## Bendy

Flag: rtcp{h0p3_y0ur3_h4v1ng_fun}
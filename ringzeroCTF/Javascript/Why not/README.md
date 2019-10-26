# Why not?

When looking at the code we can see that the user is `administrator`. This time the password is manipulated then compared to an array of values. We can use a few simple lines of python to reverse this:
```
>>> u = "administrator"
>>> values = [176,214,205,246,264,255,227,237,242,244,265,270,283]
>>> for i in range(len(u)):
	print(chr(values[i] - ord(u[i]) - i*10), end='')

	
OhLord4309111
```
The password is `OhLord4309111`

Flag: FLAG-65t23674o6N2NehA44272G24

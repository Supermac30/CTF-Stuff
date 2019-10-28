# Hash me if you can

To solve this problem I used selenium in a python REPL. First after opening up a selenium browser go to ringzero and sign in. Then compile this function and run it:
```python
def solve():
	import hashlib
	HEADER = "----- BEGIN MESSAGE -----\n"
	ENDING = "\n----- END MESSAGE -----"
	browser.get("https://ringzer0ctf.com/challenges/13")
	message = browser.find_element_by_class_name('message').text.replace(HEADER, "").replace(ENDING, "")
	#print(message)
	browser.get("https://ringzer0ctf.com/challenges/13/"+hashlib.sha512(bytes(message, encoding='utf-8')).hexdigest())
```

Looking at the webpage we should see the flag.

flag: FLAG-mukgu5g2w932t2kx1nqnhhlhy4

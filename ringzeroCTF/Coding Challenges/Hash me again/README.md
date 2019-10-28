# Hash me again

We can solve this the exact same way we solved Hash me if you can, but this time we have to remember to convert the message from binary to ascii. [This](https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa) was helpful. Remember to open import selenium and sign in first.
```
def solve():
	import hashlib
	HEADER = "----- BEGIN MESSAGE -----\n"
	ENDING = "\n----- END MESSAGE -----"
	browser.get("https://ringzer0ctf.com/challenges/14")
	message = browser.find_element_by_class_name('message').text.replace(HEADER, "").replace(ENDING, "")
	message = int(message, 2)
	message = message.to_bytes((message.bit_length() +7) // 8, 'ascii').decode()
	#print(message)
	browser.get("https://ringzer0ctf.com/challenges/14/"+hashlib.sha512(bytes(message, encoding='utf-8')).hexdigest())
```

Flag: FLAG-jz145p93ei75buh1kpx9bul9xl
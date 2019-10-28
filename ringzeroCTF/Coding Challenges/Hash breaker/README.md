# Hash breaker

Looking at the hashes in an online [hash cracker](https://crackstation.net/) we see that they are small numbers hashed with SHA1. This means to solve this challenge we only need to loop until we find a hash that matches the one on the website and print the answer. Remember to set the broser variable as the selenium browser, and to login before running solve.
```python
def solve():
	import hashlib
	HEADER = "----- BEGIN MESSAGE -----\n"
	ENDING = "\n----- END MESSAGE -----"
	browser.get("https://ringzer0ctf.com/challenges/56")
	message = browser.find_element_by_class_name('message').text.replace(HEADER, "").replace(ENDING, "")
	answer = ""
	#print(message)
	for i in range(1, 10000):
		answer = hashlib.sha1(bytes(str(i), 'utf-8')).hexdigest()
		if answer == message:
			answer = str(i)
			break
	#print(answer)
	browser.get("https://ringzer0ctf.com/challenges/56/"+answer)
```
Flag: FLAG-G1095M88Tk837G9AC0EA6q3N
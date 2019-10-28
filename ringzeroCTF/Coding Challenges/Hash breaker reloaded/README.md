# Hash breaker reloaded

This time we are given a salted hash. We can solve this exactly the same way as before but this time taking into account the fact that there are multiple message divs and that we have to add the salt before hashing. Remember to set the variable browser as your driver and login before running solve.
```
def solve():
	import hashlib
	HEADER0 = "----- BEGIN HASH -----\n"
	ENDING0 = "\n----- END HASH -----"
	HEADER1 = "----- BEGIN SALT -----\n"
	ENDING1 = "\n----- END SALT -----"
	browser.get("https://ringzer0ctf.com/challenges/57")
	messages = []
	messages = browser.find_element_by_class_name('message')
	hashinp = messages[0].text.replace(HEADER0, "").replace(ENDING0, "")
	saltinp = messages[1].text.replace(HEADER1, "").replace(ENDING1, "")
	answer = ""
	#print(message)
	for i in range(1, 10000):
		answer = hashlib.sha1(bytes(str(i) + saltinp, 'utf-8')).hexdigest()
		if answer == hashinp:
			answer = str(i)
			break
	#print(answer)
	browser.get("https://ringzer0ctf.com/challenges/57/"+answer)
```
Flag: FLAG-XJg5635WZ16F63IcE5ychgNm
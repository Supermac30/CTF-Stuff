# Can you help me find the answer to this equation

To solve this we have to split the input into parts, convert the numbers to base 10, then add and subtract them. Remember to import selenium, open a browser in the variable browser, then sign in before running solve.
```
def solve():
	import hashlib
	HEADER = "----- BEGIN MESSAGE -----\n"
	ENDING = "\n----- END MESSAGE -----"
	browser.get("https://ringzer0ctf.com/challenges/32")
	message = browser.find_element_by_class_name('message').text.replace(HEADER, "").replace(ENDING, "")
	message = message[:-4]
	message = message.split(" ")
	answer = str(message[0] + int(message[2], 16) - int(message[4], 2))
	browser.get("https://ringzer0ctf.com/challenges/32/"+answer)
```

Flag: FLAG-JsxIhjHJekAiVaxJlNe2PAYZ
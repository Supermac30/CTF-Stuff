"""
	This script tries all possibilities of ceaser shifts
	Press enter to see the next one
"""
def shift(letter, amount):
    return chr(ord('A')+((ord(letter)-amount-ord("A"))%26))
ciphertext = "CGULKVIPFRGDOOCSJTRRVMORCQDZG"
for i in range(27):
    fixed = ""
    for j in range(len(ciphertext)):
        fixed += shift(ciphertext[j],i-j)
    print(fixed)
    input()

"""
    Finds the ascii value of 'A' adds the number in the plaintext before converting back to ascii
    Output: PICOCTFTHENUMBERSMASON
"""

def decode(numbers):
    flag = ""
    for number in numbers:
        flag+= chr(ord("A")+number-1)
    return flag


cyphertext = [16, 9, 3, 15, 3, 20, 6, 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]
print(decode(cyphertext))

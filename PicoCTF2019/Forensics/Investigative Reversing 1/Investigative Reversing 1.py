"""
    This script does the opposite of what the binary does.
    Output: picoCTF{An0tha_1_8aa498d9}
"""

pic0 = "CF{An1_8aa498d9}"
pic1 = "…s"
pic2 = "icT0tha_"

flag = "picoCT"

flag += pic0[1:5]
flag += pic2[3:]
flag += pic0[5:]

print(flag)

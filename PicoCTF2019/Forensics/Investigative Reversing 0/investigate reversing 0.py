"""
    The code below does what the binary does to the flag in reverse.
    Output: picoCTF₧f0und_1t_fb69f6c2}
    For some reason I couldn't get the opening curly bracket to display, but replacing the character after 'CTF' with '{' results in the flag 
"""
text = "picoCTK€k5zsid6q_fb69f6c2}"
flag = ""
for i in range(len(text)):
    if i < 6:
        flag += text[i]
    elif i < 0xf:
        flag += chr(ord(text[i])-0x05)
    elif i == 0xf:
        flag += chr(ord(text[i])+3)
    elif i < 0x1a:
        flag += chr(ord(text[i]))
print(flag)

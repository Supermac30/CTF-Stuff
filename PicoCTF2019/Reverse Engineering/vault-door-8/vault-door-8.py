"""
    This does the reverse of what the script does, resulting in the flag.
    Output: s0m3_m0r3_b1t_sh1fTiNg_1169cac67
"""
def reverseScramble(value):
    num = list(bin(value)[2:])
    while len(num) != 8:
        num.insert(0, 0)
    num[6], num[7] = num[7], num[6]
    num[2], num[5] = num[5], num[2]
    num[3], num[4] = num[4], num[3]
    num[0], num[1] = num[1], num[0]
    num[4], num[7] = num[7], num[4]
    num[5], num[6] = num[6], num[5]
    num[0], num[3] = num[3], num[0]
    num[1], num[2] = num[2], num[1]
    return int(''.join(list(map(str, num))), 2)

values = [0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xD0, 0xD0, 0xE1, 0xD2, 0xB4, 0x94, 0xB4, 0xE1, 0xF1]
flag = ""
for value in values:
    num = reverseScramble(value)
    flag += num.to_bytes((num.bit_length() + 7) // 8, 'big').decode()
print(flag)

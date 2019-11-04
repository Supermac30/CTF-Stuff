"""
	This the function taken from the source code but run through a text
	editor replacing characters to make the syntax valid
	Output: d35cr4mbl3_tH3_cH4r4cT3r5_03b7a0
"""


def main():
	password = [None]*32
	password[0]  = 'd'
	password[29] = '7'
	password[4]  = 'r'
	password[2]  = '5'
	password[23] = 'r'
	password[3]  = 'c'
	password[17] = '4'
	password[1]  = '3'
	password[7]  = 'b'
	password[10] = '_'
	password[5]  = '4'
	password[9]  = '3'
	password[11] = 't'
	password[15] = 'c'
	password[8]  = 'l'
	password[12] = 'H'
	password[20] = 'c'
	password[14] = '_'
	password[6]  = 'm'
	password[24] = '5'
	password[18] = 'r'
	password[13] = '3'
	password[19] = '4'
	password[21] = 'T'
	password[16] = 'H'
	password[27] = '3'
	password[30] = 'a'
	password[25] = '_'
	password[22] = '3'
	password[28] = 'b'
	password[26] = '0'
	password[31] = '0'
	print(''.join(password))


main()

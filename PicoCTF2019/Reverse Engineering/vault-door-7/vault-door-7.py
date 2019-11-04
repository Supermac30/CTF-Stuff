"""
    This code takes all the numbers in the checkPassword function and converts them to binary then concatinates them. It then prints out the ascii value the binary represents.
    Output: A_b1t_0f_b1t_sh1fTiNg_fe1e495a1c
"""
int_array = [1096770097,1952395366,1600270708,1601398833,1716808014,1734305381,828716089,895562083]
binary_array = [0]*8
for i in range(len(int_array)):
    binary_array[i] = bin(int_array[i])[2:]
    while len(binary_array[i]) != 32:
        binary_array[i] = "0" + binary_array[i]
num = int(''.join(binary_array), 2)
print(num.to_bytes((num.bit_length() + 7) // 8, 'big').decode())

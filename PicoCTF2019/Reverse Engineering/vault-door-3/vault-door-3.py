"""
    This code finds the flag by moving the characters in exactly the same way checkPassword does
    Output: picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_e9af18}
"""
changed = "jU5t_a_sna_3lpm11ga4e_u_4_m9rf48"
flag = [None]*32
for i in range(8):
    flag[i] = changed[i]
for i in range(8, 16):
    flag[i] = changed[23-i]
for i in range(16, 32, 2):
    flag[i] = changed[46-i]
for i in range(31, 16, -2):
    flag[i] = changed[i]
print("picoCTF{" + ''.join(flag) + "}")

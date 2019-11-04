# vault-door-3
#### This vault uses for-loops and byte arrays. The source code for this vault is here: [VaultDoor3.java](https://2019shell1.picoctf.com/static/cf3e86645522f831c58dba985b23dc04/VaultDoor3.java)

Looking at the source we see the function checkPassword which rearranges our input and checks if it is equal to the string 'jU5t_a_sna_3lpm11ga4e_u_4_m9rf48'.
By performing the changes to the string we can return to the original password. The script above does exactly this and returns the flag.

Flag: picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_e9af18}

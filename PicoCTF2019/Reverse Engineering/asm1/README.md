# asm1
#### What does asm1(0x1b4) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](https://2019shell1.picoctf.com/static/dd43e4638ccfc5209f453733eb971da1/test.S) located in the directory at /problems/asm1_3_afba952b3219ced79409c353bf73fbd8.

The input to a function is stored in DWORD PTR [ebp+0x8]. Knowing this we can use [conditional jumps](https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm) to find that the output is just 0x1b4+0x13.

Flag: 0x1c7

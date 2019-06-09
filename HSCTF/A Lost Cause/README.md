# A Lost Cause
## Problem Statement
194 points

Written by: Disha Name Credits: Shray

Pirate Keith loves cryptography and has protected his treasure with a very annoying caesar shift. 
He has witten “CGULKVIPFRGDOOCSJTRRVMORCQDZG” on his treasure chest and has left a piece of paper with the following message: 
“every subsequent letter is shifted one less than the previous.” Knowing this, can you unlock Pirate Keith’s treasure chest?

## Solution
Ceasar ciphers are always very easy break. This is because there are always at most 26 tries needed until the solution is found.
The ad hoc cipher above is no different, since each subsequent letter decreases the shift by one it is clear there is only one 
possibility for each starting shift, and the starting shift can only be a number from 0 to 26. The script written above solves
this problem by bruteforcing until the plaintext is found. Notably I had to check if the shift was forward or backwards, but 
this involved the simple changing of line 6 and subtracting amount.

Running 'A Lost Cause.py' results in the desired plaintext and the following output:
```
INCUUGUCTGWUGHWNFQPQVNQUGVJGO

HMBTTFTBSFVTFGVMEPOPUMPTFUIFN

GLASSESAREUSEFULDONOTLOSETHEM

FKZRRDRZQDTRDETKCNMNSKNRDSGDL

EJYQQCQYPCSQCDSJBMLMRJMQCRFCK
```

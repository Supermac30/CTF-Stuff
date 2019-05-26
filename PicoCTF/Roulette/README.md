# Roulette
## Problem Statement
This Online Roulette Service is in Beta. Can you find a way to win $1,000,000,000 and get the flag? [Source](https://2018shell.picoctf.com/static/99e25c3aa326727c36a60045af958d02/auth.c). Connect with nc 2018shell.picoctf.com 25443. Hint: There are 2 bugs! 

## Solution
Looking at the source code for this problem two thing stands out,
1. The indentation is vomit inducing
2. The spins aren't cryptographically secure

Line 166 decides the spin,
```C
printf("Spinning the Roulette for a chance to win $%lu!\n", 2*bet);
long spin = (rand() % ROULETTE_SIZE)+1;
```
Here rand() is used which according to http://www.cplusplus.com/reference/cstdlib/rand/
> Returns a pseudo-random integral number in the range between 0 and RAND_MAX.
> This algorithm uses a seed to generate the series, which should be initialized to some distinctive value using function srand.

That means we should be looking for an srand, which we indeed find in line 52
```C
long get_rand() {
  long seed;
  FILE *f = fopen("/dev/urandom", "r");
  fread(&seed, sizeof(seed), 1, f);
  fclose(f);
  seed = seed % 5000;
  if (seed < 0) seed = seed * -1;
  srand(seed);
  return seed;
}
```

get_rand() is called in line 185
```C
cash = get_rand();
```

Aha! We have found the first bug. The seed is the starting cash value. Using the script "notRandom.c" and inputing the starting cash value will give us the value of every spin. We have to remember to take into account the fact a message is chosen randomly in line 172 `puts(win_msgs[rand()%NUM_WIN_MSGS]);` which means every second random value is the spin.

We cannot win only knowing this however, the program stops after 16 wins and given the max start value is 5000 doubling at each turn we need at least 19 wins.

Looking through the code we find the fishy functions:
```C
int is_digit(char c) {
    return '0' <= c && c <= '9';
}

long get_long() {
    printf("> ");
    uint64_t l = 0;
    char c = 0;
    while(!is_digit(c))
      c = getchar();
    while(is_digit(c)) {
      if(l >= LONG_MAX) {
	      l = LONG_MAX;
      	break;
      }
      l *= 10;
      l += c - '0';
      c = getchar();
    }
    while(c != '\n')
      c = getchar();
    return l;
}
```
instead of a simple fgets() this function uses a wierdly complicated checking system.
This function is called in line 60 `long bet = get_long();` it takes the value we input and sets it to the bet.

This function reads only digits and stops when the digits stop appearing. It is also impossible to input a number longer than LONG_MAX because of the check which means no integer overflow. 

At first I thought the bug had something to do with the getchar() function, but then I realised that the check to stop an integer overflow happens after variable l changes. Boom! We have found the second bug. By inputing a number the same length as LONG_MAX but is infact larger we can easily overflow the integer and return a negative number.

This is useful because a negative number would pass the check on line 61:
```C
if(bet <= cash) {
  return bet;
} else {
  puts("You can't bet more than you have!");
}
```
and would be able to increase the money we have on line 195 `cash -= bet;` all we have to do is lose, and our cash would stay at its increased value.

The problem with this however is that we need to have 3 games before or else we are denied the flag. This is where bug 1 comes in handy.

Combining the two bugs by winning three times in the beginning then betting a value like 3147483647 would result in when running the script with the starting value and betting correctly
```
supermac30@Mark-Laptop:~/cStuff$ ./breakRoulette
1215
bet: 13
bet: 33
bet: 11
don't bet: 9
```
```
Welcome to ONLINE ROULETTE!
Here, have $1215 to start on the house! You'll lose it all anyways >:)

How much will you wager?
Current Balance: $1215   Current Wins: 0
> 1
Choose a number (1-36)
> 13

Spinning the Roulette for a chance to win $2!

Roulette  :  13

Wow.. Nice One!

How much will you wager?
Current Balance: $1216   Current Wins: 1
> 1
Choose a number (1-36)
> 33

Spinning the Roulette for a chance to win $2!

Roulette  :  33

Darn, you got it right.

How much will you wager?
Current Balance: $1217   Current Wins: 2
> 1
Choose a number (1-36)
> 11

Spinning the Roulette for a chance to win $2!

Roulette  :  11

Congrats!

How much will you wager?
Current Balance: $1218   Current Wins: 3
> 3147483647
Choose a number (1-36)
> 8

Spinning the Roulette for a chance to win $1999999998!

Roulette  :  9

Nice try..
If you keep it up, maybe you'll get the flag in 100000000000 years

*** Current Balance: $1147484867 ***
Wow, I can't believe you did it.. You deserve this flag!
picoCTF{1_h0p3_y0u_f0uNd_b0tH_bUg5_8b7aef91}
```

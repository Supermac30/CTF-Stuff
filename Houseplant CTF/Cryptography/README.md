# Cryptography
This file contains my solutions for the crypto problems in the houseplant CTF

## CH₃COOH
Looking at the ciphertext we see that the text maintained its spacing, only the letters themselves changed. This suggests a substitution cipher of ployalphabetic cipher was used. We can decode the ciphertext with an [online tool](https://www.guballa.de/vigenere-solver)

Flag:  rtcp{vinegar_on_my_fish_and_chips_please}

## "fences are cool unless they're taller than you" - tida
The flag is encrypted with a rail fence cipher. We can use an [online tool](https://crypto.interactive-maths.com/rail-fence-cipher.html) to decrypt it.

Flag: rtcp{ask_tida_about_rice_washing}

## Returning Stolen Archives
The key insight to solving this problem is that because the message is encrypted byte by byte the message space is tiny!
This means we can brute force each character and find the flag. The script in this file does exactly that.

Flag: rtcp{cH4r_bY_Ch@R!}

## Broken Yolks
We are given an anagram which we have to solve. Playing around with the text I found the word scrambled, I then used [this online tool](http://boulter.com/anagram/) to solve the rest.

Flag: rtcp{scrambled_or_fried}

## Rivest Shamir Adleman
We are given a file called component.txt. Looking through the generate_keys.py file we see that one of the primes is dumped here. With this information, and n from the public key, we can find d. Going into the decrypt.py file and running it with the private key we found results in the flag.

flag: rtcp{f1xed_pr\*me-0r_low_e?}

## Post-Homework Death
We are given a decoding matrix and a ciphertext, after turning the ciphertext into a matrix, finding the plaintext is as easy as multiplying the decoding matrix with the ciphertext matrix. [This site](http://aix1.uottawa.ca/~jkhoury/cryptography.htm) was very helpful.

Flag: rtcp{go_do_your_homework}

## Parasite
Looking at the problem statement we see that some characters are capitalized. Putting them together we get the word SKATS. SKATS stands for Standard Korean Alphabet Transliteration System and is a system for mapping morse code to Hangul, Korean script. 

I couldn't find an online tool for converting morse to English through SKATS so I did it manually. Using cybertools to decode the morse to English letters, we can then use the chart [here](https://en.wikipedia.org/wiki/SKATS) to turn the letters to Hangul. We would result in:
```
ㅎ  ㅡ  ㅣ    ㅁ  ㅏ  ㅇ     ㅇ  ㅡ  ㄴ     ㅈ  ㅣ  ㄴ     ㅈ  ㅓ  ㅇ    ㅎ  ㅏ  ㄴ    ㄱ  ㅣ    ㅅ  ㅏ  ㅣ  ㅇ    ㅊ  ㅜ  ㅇ    ㅇ  ㅣ  ㅂ   ㄴ  ㅣ    ㄷ  ㅏ
```
We can then use an [online keyboard](https://www.lexilogos.com/keyboard/korean.htm) to put the letters together like so:
```
희망은진정한기생충입니다
```
Translating this results in the flag.

Flag: rtcp{hope_is_a_true_parasite}

## Sizzle
The file we are given is actually a binary encoded string. Replacing all the '.' with 1 and the '-' with 0 results in the flag.

Flag: rtcp{bacon_but_grilled_and_morsified}

## Rainbow Vomit
The image uses a hexahue encoding to hide the flag. Decoding all of the image is too much by hand, however the flag is clearly contained at the bottom, as the amount of numbers increases and there is a clear starting and ending point for the flag.

We can use an [online chart](https://www.geocachingtoolbox.com/index.php?lang=en&page=hexahue) to quickly find the flag.

Flag: rtcp{SHOULD,FL5G4,B3,ST1CKY,OR,N0T}
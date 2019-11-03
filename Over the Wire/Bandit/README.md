# Bandit
This readme contains the solutions to the entry level wargaming challenge Bandit.

## Level 0
Connecting to the server with ssh then reading the readme file results in the password.

Password: boJ9jbbUNNfktd78OOpsqOltutMc3MY1

## Level 1
This time to read the file we can run:
```
bandit1@bandit:~$ cat ./-
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
```
Password: CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

## Level 2
Surrounding the filename with speech marks results in the password.
```
bandit2@bandit:~$ cat "spaces in this filename"
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
```
Password: UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

## Level 3
Running `ls -a` we can see all th ehidden file containing the flag.
```
bandit3@bandit:~$ cd inhere
bandit3@bandit:~/inhere$ ls
bandit3@bandit:~/inhere$ ls -a
.  ..  .hidden
bandit3@bandit:~/inhere$ cat .hidden
pIwrPrtPN36QITSp3EQaw936yaFoFgAB
```
Password: pIwrPrtPN36QITSp3EQaw936yaFoFgAB

## Level 4
We can try searching all the files for a human readable character, like 0, using rgrep.
```
bandit4@bandit:~/inhere$ rgrep 0
-file07:koReBOKuIDDepwhWk7jZC0RTdopnAYKh
```
Password: koReBOKuIDDepwhWk7jZC0RTdopnAYKh

## Level 5
Using the find command we can search for all files of size 1033 bytes.
```
bandit5@bandit:~/inhere$ find -type f -size 1033c
./maybehere07/.file2
bandit5@bandit:~/inhere$ cd maybehere07
bandit5@bandit:~/inhere/maybehere07$ cat .file2
DXjZPULLxYr17uwoI01bNLQbtFemEgo7
```
Password: DXjZPULLxYr17uwoI01bNLQbtFemEgo7

## Level 6
If we exit to the first highest directory and search through all files for a file 33 bytes large and has bandit6 in the file name. We can use this command then search for the line with no permission denied `find -type f -size 33c -user bandit7`.

```
bandit6@bandit:/$ cat ./var/lib/dpkg/info/bandit7.password
HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
```
Password: HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs

## Level 7
We can search for the word millionth in the file using grep.
```
bandit7@bandit:~$ grep millionth data.txt
millionth       cvX2JJa4CFALtqS87jk27qwqGhBM9plV
```
Password: cvX2JJa4CFALtqS87jk27qwqGhBM9plV

## Level 8
We can sort the file with `sort data.txt` then use `uniq -c` to print out the number of times each line is repeated by searching for the line with 1 with `grep -w 1`.
```
bandit8@bandit:~$ sort data.txt | uniq -c | grep -w 1
      1 UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
```
Password: UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR

## Level 9
Searching the strings in the file for lines with a '=' results in the flag.
```
bandit9@bandit:~$ strings data.txt | grep ==
2========== the
========== password
========== isa
========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
```
Flag: truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk

## Level 10
Searching for the line with an equal results in the base64 encoded data. Running it through `base64 -d` results in the password.
```
bandit10@bandit:~$ strings data.txt | grep = | base64 -d
The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
```
Password: IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR

## Level 11
Running the output through an online rot13 decoder results in the password.

Password: 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu

## Level 12
To solve this problem I first copied the file data to a text editor and removed the addresses and ascii on the side. after running `xxd -r -p <<"END" > out.gz` I decompressed the file using `gzip -d`. After going through each compression we can check how it is compressed using file and use the appropriate command. `tar -xvf` for tar files, `bzip -d` for bzip archives, `gzip -d` for gzip archives. After fully decompressing the file we get the following text:
```
bandit12@bandit:/tmp/mac$ cat data8
The password is 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
```

## Level 13
To solve this challenge I copied the file to my computer, made it root only `chmod 600 sshkey.private` then used this command to connect with it as an ssh key `ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220`.

## Level 14
Looking in the etc folder we find that the current password is `4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e`. We can submit this to localhost with netcat to find the password for the next level.
```
bandit14@bandit:/etc/bandit_pass$ cat bandit14 | nc localhost 30000
Correct!
BfMYroe26WYalil77FoDi9qh59eK5xNr
```
Password: BfMYroe26WYalil77FoDi9qh59eK5xNr

## Level 15
To solve this problem we can connect with openssl using the command `openssl s_client -connect localhost:30001` and send the password by typing it in after connecting

Password: cluFn7wTiGryunymYOu4RcffSxQluehd

## Level 16
Running nmap we can find the open port in the range provided:
```
bandit16@bandit:~$ nmap -p 31000-32000 localhost

Starting Nmap 7.40 ( https://nmap.org ) at 2019-11-02 06:28 CET    Nmap scan report for localhost (127.0.0.1)
Host is up (0.00021s latency).
Not shown: 999 closed ports
PORT      STATE    SERVICE
31518/tcp filtered unknown
31790/tcp open     unknown

Nmap done: 1 IP address (1 host up) scanned in 1.26 seconds
```
We can send the last password with openssl to complete the challenge. We get a key which we can use to get to the next challenge.

## Level 17
Using the diff command we can find the line that has been changed.
```
bandit17@bandit:~$ diff passwords.old passwords.new
42c42
< hlbSBPAWJmL6WFDb06gpTx1pPButblOA
---
> kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
```

Password: kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd

## Level 18
We can add a cat command after the ssh command to bypass .bashrc
```
supermac30@LAPTOP-D0Q1SN5H:~/test$ ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password:
IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
```
Password: IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x

## Level 19
We can cat the password file as the user bandit20 to get the password.
```
bandit19@bandit:~$ ./bandit20-do cat /etc/bandit_pass/bandit20
GbKksEFF4yrVs6il55v6gwY5aVje5f0j
```
Password: GbKksEFF4yrVs6il55v6gwY5aVje5f0j

## Level 20
We need to terminals to solve this problem. We could use tmux, screen, or we can just login twice. We need to listen on a port with `nc -l 1111` on one of the terminals and connect to it with suconnect on the other terminal. Sending the last password through the server results in the password.

Password: gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr

## Level 21
Looking in /etc.cron.d we can see that the program `/usr/bin/cronjob_bandit22.sh` is running at regular intervals. Looking at the source we see that it puts the password in some file in the temp directory. Reading it results in the flag.
```
bandit21@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit22.sh
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
bandit21@bandit:/etc/cron.d$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
```
Password: Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI

## Level 22
To solve this challenge we have to realise that the code is storing the password at a predictable location.
```
bandit22@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit23.sh
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)      
echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
```
If we can find mytarget when myname is bandit23 we can find the password. Running this results in the password:
```
bandit22@bandit:/etc/cron.d$ myname=bandit23
bandit22@bandit:/etc/cron.d$ echo I am user $myname | md5sum | cut -d ' ' -f 1
8ca319486bfbbc3663ea0fbe81326349
bandit22@bandit:/etc/cron.d$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349
jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n
```

Password: jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n

## Level 23
If we make a script in the directory '/var/spool/bandit24' that puts the password in a file in the tmp directory then wait for the cron job to run it we can get the password. The part that got me stuck was setting the permissions of the files so that the script can read and write to them.
```
bandit23@bandit:/etc$ cd /tmp
bandit23@bandit:/tmp$ mkdir mac1
bandit23@bandit:/tmp$ cd mac1
bandit23@bandit:/tmp/mac1$ touch password
bandit23@bandit:/tmp/mac1$ chmod 666 password
bandit23@bandit:/tmp/mac1$ cd /var/spool/bandit24
bandit23@bandit:/var/spool/bandit24$ touch script.sh
bandit23@bandit:/var/spool/bandit24$ echo "cat /etc/bandit_pass/bandit24 > /tmp/mac1/password" > script.sh
bandit23@bandit:/var/spool/bandit24$ chmod 777 script.sh
bandit23@bandit:/var/spool/bandit24$ cd /tmp/mac1
bandit23@bandit:/tmp/mac1$ cat password
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
```

Password: UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ

## Level 24
We can write a simple script to brute force the connection. [This SO exchange](https://stackoverflow.com/questions/33338128/netcat-with-milliseconds-interval) was particularly helpful.
```
bandit24@bandit:/tmp/mac2$ while read -r line; do echo "$line"; sleep 0.001; done < try.txt | nc localhost 30002 | grep -v Wrong!
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
Correct!
The password of user bandit25 is uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG  
Exiting.
```
Password: uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG

## Level 25
I couldn't solve this problem on my own. I had to read a writeup, the solution is surprisingly cool.

Looking in the /etc/passwd file we see that bandit26's shell is stored in the file '/usr/bin/showtext'. Looking inside we see:
```
bandit25@bandit:/etc$ cat /usr/bin/showtext
#!/bin/sh

export TERM=linux

more ~/text.txt
exit 0
```
The more command here is especially important. We can shrink our terminal to force the more command to run, then press v to open vim on the file. While in vim we can use the command `:e! /etc/bandit_pass/bandit26` to open the password file in vim.

Password: 5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z

## Level 26
We can change the shell in vim using `:set shell=/bin/bash`. We can then use the bandit27-do file to read the password.
```
bandit26@bandit:~$ ./bandit27-do cat /etc/bandit_pass/bandit27
3ba3118a22e93127a4ed485be72ef5ea
```
Password: 3ba3118a22e93127a4ed485be72ef5ea

## Level 27
Creating a directory in the tmp folder and cloning the repository there results in the password.
```
bandit27@bandit:/tmp/mac3$ git clone ssh://bandit27-git@localhost/home/bandit27-git/repo
Cloning into 'repo'...
Could not create directory '/home/bandit27/.ssh'.
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is SHA256:98UL0ZWr85496EtCRkKlo20X3OPnyPSB5tB5RPbhczc.
Are you sure you want to continue connecting (yes/no)? yes
Failed to add the host to the list of known hosts (/home/bandit27/.ssh/known_hosts).
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit27-git@localhost's password:
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0)
Receiving objects: 100% (3/3), done.
bandit27@bandit:/tmp/mac3$ cat repo/README
The password to the next level is: 0ef186ac70e04ea33b4c1853d2526fa2
```
Password: 0ef186ac70e04ea33b4c1853d2526fa2

## Level 28
Looking at the log with the command `git log -p README.md` we see that the password was commited then removed. We can find the password in the output of the command.

Password: bbc96594b4e001778eee9975372716b2

## Level 29
Looking at the branches with `git branch -av` we can see that there exists a dev branch. Going to the dev branch with `git checkout dev` and reading the README.md file results in the flag.

Password: 5b90576bedb2cc04c86a9e924ce42faf

## Level 30
With the command `git tag` we can see that the tag 'secret' exists. We can read it with `git show secret` to get the password.

Password: 47e603bb428404d265f59c42920d81e5

## Level 31
After cloning the repo we can use the commands `touch key.txt` then `git add -f key.txt` to add a new file. We can then add the required text with `echo "May I come in?" > key.txt`. Then we should commit the file with `git commit key.txt`. Lastly, we can push the file with `git push origin master` to get the flag.

Password: 56a9bf19c63d650ce78e6ec0354ee45e

## Level 32
We need a command that does not contain any lowercase letters to bypass the filter. Using the positional parameter `$0` to create a bash shell does the trick.
```
WELCOME TO THE UPPERCASE SHELL
>> $0
$ cat /etc/bandit_pass/bandit33
c9c3199ddf4121b10cf581a98d51caee
```
Password: c9c3199ddf4121b10cf581a98d51caee
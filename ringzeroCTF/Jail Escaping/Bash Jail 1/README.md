# Bash Jail 1

When connecting we can see that we are trapped in a program that executes anything we give it. We can execute '/bin/bash' to gain access to the terminal. The problem is that we can only see stderr and not stdout. To fix this we can [redirect the output to stderr](https://stackoverflow.com/questions/2990414/echo-that-outputs-to-stderr). This results in the flag.
```
Your input:
/bin/bash
level1@lxc17-bash-jail:~$ >&2 cat flag.txt
FLAG-U96l4k6m72a051GgE5EN0rA85499172K
```

Flag: FLAG-U96l4k6m72a051GgE5EN0rA85499172K

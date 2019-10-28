# Challenge Access list

To solve this challenge we first have to find a way to inject sql. Looking at the source we can see that there is a value we can change at `<option value="admin">`. Changing it to `' OR '` doesn't result in an error.


Here we can inject our sql. Changing the line to this `<option value="' or Username='charles">` to see everyone whos name is charles results in the flag.

Flag: FLAG-sdfoip340e89rfuj34woit
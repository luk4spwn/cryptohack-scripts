# Great Snakes
For this challenge we are provided with the following script

``` python
#!/usr/bin/env python3

import sys
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]

print("Here is your flag:")
print("".join(chr(o ^ 0x32) for o in ords))
```
When executed, it gives us the flag to solve the challenge..

``` shell
➜  great_snakes git:(main) python3 great_snakes_35381fca29d68d8f3f25c9fa0a9026fb.py
Here is your flag:
crypto{z3n_0f_pyth0n}
```
## Explanation

We can see that the script imports the `sys` library, this to detect if the Python version is greater than 2 in this line of code.

``` python
if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")
```

Then, we have an array called `ords` that has 21 numbers.

``` python
ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]
```

The numbers in this array are letters in their decimal representation, we can look at the ASCII tables to check this.

![](https://i.imgur.com/nqDnf3s.png)

At the end of the script, using the chr() function returns a string containing the character associated with the specified character code. and applies an XOR function `^` with `0x32`.

``` shell
>>> chr(81 ^ 0x32)
'c'
>>>
```

# XOR Starter

For this challenge we are given the following statement.

```
XOR is a bitwise operator which returns 0 if the bits are the same, and 1 otherwise. In textbooks the XOR operator is denoted by ⊕, but in most challenges and programming languages you will see the caret ^ used instead.


A	B	Output
0	0	0
0	1	1
1	0	1
1	1	0

For longer binary numbers we XOR bit by bit: 0110 ^ 1010 = 1100. We can XOR integers by first converting the integer from decimal to binary. We can XOR strings by first converting each character to the integer representing the Unicode character.

Given the string label, XOR each character with the integer 13. Convert these integers back to a string and submit the flag as crypto{new_string}.

The Python pwntools library has a convenient xor() function that can XOR together data of different types and lengths. But first, you may want to implement your own function to solve this. 
```

They explain that xor is a bitwise operator that returns 0 if the bits are equal to 1 (we can see in the example table).

Also, for longer binary numbers we apply the bitwise XOR `0110 ^ 1010 = 1100`, we can XOR integers by first converting the decimal number to binary, finally we are told that we have to XOR the string `label` with the key `13`. I programmed the following python script to solve the challenge.

``` python
string = "label"

print("crypto{", end="")
for x in string:
    print(chr(ord(x)^13), end="")
print("}")
```

When running it

``` shell
➜  6-xor_starter git:(main) ✗ python3 decrypt.py
crypto{aloha}
```

> Let's remember that ^ is used for XOR, important...
# Favourite byte

For this challenge we are given the following statement.

```
For the next few challenges, you'll use what you've just learned to solve some more XOR puzzles.

I've hidden some data using XOR with a single byte, but that byte is a secret. Don't forget to decode from hex first.

73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d
```

They explain that they have hidden some data using XOR with a single byte and pass us the encoded string.

By logic if the string was encoded with a pure byte the key is insecure, so let's program a Python script to brute force the string.

``` python
from pwn import xor
text_cipher = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for i in range(255):
    if b'crypto' in xor(text_cipher, i):
        print(xor(text_cipher, i))
        exit()
print('Not found')
```

## Explanation

Following the code first creates a variable called `text_cipher` which stores the encoded string.

Then start a for where `i` will be worth the values of `range(255)`, and then with an if it checks if the crypto string is present by applying an xor function with the encrypted string and using i as the key, if it is present, it prints the decrypted text on the screen.

When executed.

``` shell
➜  8-favourite_byte git:(main) ✗ python3 brute_forcer.py
b'crypto{0x10_15_my_f4v0ur173_by7e}
```

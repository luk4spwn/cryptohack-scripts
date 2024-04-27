# Bytes and big Integers

For this challenge we are given the following statement.

```
Cryptosystems like RSA works on numbers, but messages are made up of characters. How should we convert our messages into numbers so that mathematical operations can be applied?

The most common way is to take the ordinal bytes of the message, convert them into hexadecimal, and concatenate. This can be interpreted as a base-16/hexadecimal number, and also represented in base-10/decimal.

To illustrate:

message: HELLO
ascii bytes: [72, 69, 76, 76, 79]
hex bytes: [0x48, 0x45, 0x4c, 0x4c, 0x4f]
base-16: 0x48454c4c4f
base-10: 310400273487

Python's PyCryptodome library implements this with the methods bytes_to_long() and long_to_bytes(). You will first have to install PyCryptodome and import it with from Crypto.Util.number import *. For more details check the FAQ.

Convert the following integer back into a message:

11515195063862318899931685488813747395775516287289682636499965282714637259206269
```

In summary they explain us that cryptosystems like RSA work with numbers, but the messages are composed of characters, the most common way to convert our messages in numbers is to convert them to hexadecimal and concatenate, this can be interpreted as a base 16/hexadecimal number and also be represented in base 10/decimal.

We can see that we are given a hint, using the `long_to_bytes()` function we can convert this string to a string. Program the following script to solve this challenge.

``` python
from Crypto.Util.number import *


print("Mensaje con long_to_bytes")
print(long_to_bytes(11515195063862318899931685488813747395775516287289682636499965282714637259206269))
```

When executed.

```
➜  5-bytes_and_big_integers git:(main) ✗ python3 solve.py
Mensaje con long_to_bytes
b'crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}'
```

# You either know, XOR you don't

For this challenge we are given the following statement.

```
I've encrypted the flag with my secret key, you'll never be able to guess it.

Remember the flag format and how it might help you in this challenge!

0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104
```

In simple words they have encrypted the flag with a secret key, as a hint they tell us that the format of the previous flag could help me to solve the challenge, following this I programmed the following script.

``` python
from pwn import xor
flag = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')

print(xor(flag, 'crypto{'.encode()))
```
## Explanation

I create a variable called flag that has the flag in hexadecimal and using `bytes.fromhex()` I convert it to bytes.

I then screen print the flag with .encode().

```
➜  9-you_either_know_XOR_you_don git:(main) ✗ python3 solve.py
b'myXORke+y_Q\x0bHOMe$~seG8bGURN\x04DFWg)a|\x1dTM!an\x7f'
```

By deduction we can see that the key used to encrypt this string is `myXORkey`, I modified the script to solve the challenge and I am left like this.

``` python
from pwn import xor
flag = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')

print(xor(flag, 'crypto{'.encode()))
print(xor(flag, 'myXORkey'.encode()))
```

When executed.

``` shell
b'crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}'
```
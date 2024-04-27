# ASCII

The following statement is provided for this section.

```
ASCII is a 7-bit encoding standard which allows the representation of text using the integers 0-127.

Using the below integer array, convert the numbers to their corresponding ASCII characters to obtain a flag.

[99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

In Python, the chr() function can be used to convert an ASCII ordinal number to a character (the ord() function does the opposite)
```

They explain that ASCII is an encoding standard that allows the representation using integers from 0 to 127, and an array with numbers that we have to decode to read the flag. To solve the challenge I programmed the following script.

``` python
flag = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

for character in flag:
    print(chr(character))
```

## Explanation

What I did was to use the `chr()` function to pass the number from decimal to string.

If you want to understand this further I invite you to read the documentation on [chr](https://www.w3schools.com/python/ref_func_chr.asp) and on the [ASCII](https://elcodigoascii.com.ar/) code.

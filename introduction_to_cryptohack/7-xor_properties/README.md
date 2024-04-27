# XOR Properties

For this challenge we are given the following statement.

```
In the last challenge, you saw how XOR worked at the level of bits. In this one, we're going to cover the properties of the XOR operation and then use them to undo a chain of operations that have encrypted a flag. Gaining an intuition for how this works will help greatly when you come to attacking real cryptosystems later, especially in the block ciphers category.

There are four main properties we should consider when we solve challenges using the XOR operator

Commutative: A ⊕ B = B ⊕ A
Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
Identity: A ⊕ 0 = A
Self-Inverse: A ⊕ A = 0

Let's break this down. Commutative means that the order of the XOR operations is not important. Associative means that a chain of operations can be carried out without order (we do not need to worry about brackets). The identity is 0, so XOR with 0 "does nothing", and lastly something XOR'd with itself returns zero.

Let's put this into practice! Below is a series of outputs where three random keys have been XOR'd together and with the flag. Use the above properties to undo the encryption in the final line to obtain the flag.

KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

Before you XOR these objects, be sure to decode from hex to bytes.
```

In summary, they explain that there are four main properties to consider when solving challenges using the XOR operator (Commutative, Associative, Identity, and Self-Inverse). Program the following script to solve it.

``` python
from pwn import xor

k1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
k2_3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
flag = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")
print(xor(k1,k2_3,flag))
```

## Explanation

The script uses the properties of the XOR operation to solve the problem:

Commutative: As we mentioned, the commutative property states that the order in which we apply XOR does not matter. In the script, the keys are applied in a specific order (k1, k2_3), but the XOR function handles this internally, so we don't need to worry about the order. The function xor(k1, k2_3, flag) performs XOR between k1, k2_3 and flag regardless of their order.

Associative: The associative property tells us that we can group the XOR operands in any way. In the script, k2_3 is a combination of the second and third keys. We could have calculated k2_3 first and then applied it together with k1 to the encrypted message, or we could have applied k1 first and then k2_3. The xor() function handles these operations without the need for explicit grouping.

Identity: The identity property tells us that XOR with zero does not change the original value. In the script, we do not explicitly see the application of identity, but we could have added ^ bytes.fromhex("0") to any of the operands without changing the result.

Self-Inverse: This property states that an XOR value with itself is zero.In the script, we do not apply this property directly, but we could have seen something like k2 ^ k2, which would result in zero.However, the xor() function takes care of automatically removing the effects of XOR with itself.

So, although the script does not explicitly use these properties, it takes advantage of them by applying the xor() function to solve the problem efficiently and correctly.
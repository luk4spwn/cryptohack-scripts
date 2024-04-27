from pwn import xor
text_cipher = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for i in range(255):
    if b'crypto' in xor(text_cipher, i):
        print(xor(text_cipher, i))
        exit()
print('Not found')

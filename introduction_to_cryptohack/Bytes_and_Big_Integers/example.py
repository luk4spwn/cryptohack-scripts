message = "HELLO"

print("\nBytes ASCII:")
for letter in message:
    print(ord(letter))

print("\nHex bytes:")
for letter in message:
    new_letter = ord(letter)
    print(hex(new_letter))

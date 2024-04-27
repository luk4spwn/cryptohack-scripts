string = "label"

print("crypto{", end="")
for x in string:
    print(chr(ord(x)^13), end="")
print("}")


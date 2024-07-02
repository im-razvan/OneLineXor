# One line XOR

xor = lambda string, key: ''.join(chr(ord(string[i]) ^ ord(key[i % len(key)])) for i in range(len(string)))

x = xor("Hello World", "key")

print(xor(x, "key")) # Hello World
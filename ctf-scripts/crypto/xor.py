#!/usr/bin/env python3
import pwn

#cipher.enc as hash
input = "134af6e1297bc4a96f6a87fe046684e8047084ee046d84c5282dd7ef292dc9"

#CTF format in letters
key = ["C", "T", "F", "{"]

for i in range(0, 2*len(key), 2):
    x = key[i//2].encode()
    y = bytes.fromhex(input[i:i+2])
    key[i//2] = pwn.xor(x, y)

def decrypt(cipher):
    plain = b''
    for i in range(0, len(cipher), 2):
        z = bytes.fromhex(cipher[i:i+2])
        plain += pwn.xor(key[(i//2)%len(key)], z)
    return plain


print(decrypt(input))

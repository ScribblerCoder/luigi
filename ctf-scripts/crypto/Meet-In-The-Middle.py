from random import randint
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def encrypt1(pt):
    alphabet = b"0123456789abcdef"
    const = b"0fpptCTF5!@#"
    keys = {}
    for a in alphabet:
        for b in alphabet:
            for c in alphabet:
                for d in alphabet:
                    key = const + bytes([a, b, c, d])
                    cipher = AES.new(key, mode=AES.MODE_ECB)
                    ct = cipher.encrypt(pad(pt, 16))
                    keys[ct] = key

    return keys


def encrypt2(ct, keys):
    alphabet = b"0123456789abcdef"
    const = b"0fpptCTF5!@#"
    for a in alphabet:
        for b in alphabet:
            for c in alphabet:
                for d in alphabet:
                    key = bytes([a, b, c, d]) + const
                    cipher = AES.new(key, mode=AES.MODE_ECB)
                    pt = cipher.decrypt(ct)
                    if pt in keys:
                        return keys[pt], key


pt1 = bytes.fromhex("4f465050542d435446")
ct1 = bytes.fromhex("f71f3b195e2336a6d30077b8184304c6")
ct2 = bytes.fromhex(
    "187f25ea856f518bcd8e7e7c17e7e6016bc77459513740e6792c84d07b465ea9cee6609881421eb4ae1606792a2d8859"
)
keys = encrypt1(pt1)
key1, key2 = encrypt2(ct1, keys)
cipher = AES.new(key2, mode=AES.MODE_ECB)
pt2 = cipher.decrypt(ct2)
cipher = AES.new(key1, mode=AES.MODE_ECB)
pt2 = cipher.decrypt(pt2)
pt2 = unpad(pt2, 16)
print(pt2)

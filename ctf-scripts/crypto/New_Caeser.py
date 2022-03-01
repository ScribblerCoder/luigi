import string


cipher = "kjlijdliljhdjdhfkfkhhjkkhhkihlhnhghekfhmhjhkhfhekfkkkjkghghjhlhghmhhhfkikfkfhm"
LOWERCASE_OFFSET = ord('a')
ALPHABET = string.ascii_lowercase[:16]

def b16_decode(enc):
	plain = ""
	for c in range(0,len(enc),2):
		binary_1 = "{0:04b}".format(ord(enc[c]) - LOWERCASE_OFFSET)
		binary_2 = "{0:04b}".format(ord(enc[c+1]) - LOWERCASE_OFFSET)
		binary = binary_1 + binary_2
		plain += chr(int(binary,2))
	return plain

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 - t2) % len(ALPHABET)]


for i,key in enumerate(string.ascii_lowercase):
	possible_string = ""
	for c in cipher:
		possible_string += shift(c,key)
	print(i)
	print(b16_decode(possible_string))
import sys
import codecs
import base64
import string


def help():
    asciiart = """
█████                               ██████████  ██████ ██████                   █████   
░░███                               ░░███░░░░░█ ███░░█████░░███                 ░░███    
 ░███         ██████  █████ ███ █████░███  █ ░ ░███ ░░░███ ░░░██████  ████████  ███████  
 ░███        ███░░███░░███ ░███░░███ ░██████  ██████████████ ███░░███░░███░░███░░░███░   
 ░███       ░███ ░███ ░███ ░███ ░███ ░███░░█ ░░░███░░░░███░ ░███ ░███ ░███ ░░░   ░███    
 ░███      █░███ ░███ ░░███████████  ░███ ░   █░███   ░███  ░███ ░███ ░███       ░███ ███
 ███████████░░██████   ░░████░████   ███████████████  █████ ░░██████  █████      ░░█████ 
░░░░░░░░░░░  ░░░░░░     ░░░░ ░░░░   ░░░░░░░░░░░░░░░  ░░░░░   ░░░░░░  ░░░░░        ░░░░░  
      ███████████                  █████                                                 
     ░░███░░░░░███                ░░███                                                  
      ░███    ░████████ ████ ████████████    ██████  ████████                            
      ░██████████░░███ ░███ ███░░░░░███░    ███░░███░░███░░███                           
      ░███░░░░░███░███ ░███░░█████ ░███    ░███████  ░███ ░░░                            
      ░███    ░███░███ ░███ ░░░░███░███ ███░███░░░   ░███                                
      ███████████ ░░██████████████ ░░█████ ░░██████  █████                               
     ░░░░░░░░░░░   ░░░░░░░░░░░░░░   ░░░░░   ░░░░░░  ░░░░░  luigi  v1.0.0"""
    print(asciiart)
    print("\n\nusage: python3 LowEffortBuster.py <file>")


def rot(flag, key):

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    result = ""
    # transverse the plain text
    for i in range(len(flag)):
        char = flag[i]

        # Encrypt uppercase characters in plain text
        if char in upper:
            result += chr((ord(char) + key - 65) % 26 + 65)


        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)

    return result.encode()


def base64(flag):
    cipher = base64.b64encode(flag)
    return cipher


def main():

    # add ctf flag format here
    Flag_Format = ""

    # add every possible encoding in this list
    ciphers = [] 
    if len(sys.argv) != 2:
        help()
        exit()

    hex_dump = open(sys.argv[1], "r").read()

    #add all ROTs
    for i in range(0, 26):
        tmp = rot(Flag_Format, i)
        ciphers.append(tmp)


main()

# encodings to add
# - ROT13 (and all possible ROTs)
# - Base64 ( and hex/decimal/octal/binary/base32/base85)
# - URL encode
# - braille
# - reverse

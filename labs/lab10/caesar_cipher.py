def encrypt(plaintext, key):
    ciphertext = []
    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted_code = (ord(char) - base + key) % 26
            new_char = chr(base + shifted_code).lower()
            ciphertext.append(new_char)
        elif char.isspace():
            ciphertext.append(char)
        elif char.isascii() and not char.isalnum():
            shifted_code = (ord(char) + key) % 128
            ciphertext.append(chr(shifted_code))
        else:
            ciphertext.append(char)
    return "".join(ciphertext)

def decrypt(ciphertext, key):
    plaintext = []
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted_code = (ord(char) - base - key) % 26
            new_char = chr(base + shifted_code).lower()
            plaintext.append(new_char)
        elif char.isspace():
            plaintext.append(char)
        elif char.isascii() and not char.isalnum():
            shifted_code = (ord(char) - key) % 128
            plaintext.append(chr(shifted_code))
        else:
            plaintext.append(char)
    return "".join(plaintext)

def main():
    print(encrypt("hello WORLD!", 3))  # Expected: "khoor zruog$"
    print(decrypt("KHOOR zruog$", 3))  # Expected: "hello world!"

    print(encrypt("zzz", 6))           # Expected: "fff"
    print(decrypt("FFF", 6))           # Expected: "zzz"

    print(encrypt("FFF", -6))          # Negative keys also work, expected "zzz"

if __name__ == "__main__":
    main()

class Caesar:
    def __init__(self, key=0):
        self._key = key  
    
    def get_key(self):
        return self._key
    
    def set_key(self, new_key):
        self._key = new_key

    def encrypt(self, plaintext):
        ciphertext = ""
        for char in plaintext:  
            if char.isalpha():  
                base = ord('A') if char.isupper() else ord('a')
                shift = (ord(char) - base + self.get_key()) % 26
                ciphertext += chr(base + shift).lower()  
            elif char.isspace():  
                ciphertext += char
            elif char.isascii() and not char.isalnum():  
                shift = (ord(char) + self.get_key()) % 128
                ciphertext += chr(shift)
            else:
                ciphertext += char  
        return ciphertext
    
    def decrypt(self, ciphertext):
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():  
                base = ord('A') if char.isupper() else ord('a')
                shift = (ord(char) - base - self.get_key()) % 26
                plaintext += chr(base + shift).lower()  
            elif char.isspace():  
                plaintext += char
            elif char.isascii() and not char.isalnum():  
                shift = (ord(char) - self.get_key()) % 128
                plaintext += chr(shift)
            else:
                plaintext += char  
        return plaintext

cipher = Caesar()
cipher.set_key(3)
# cipher.key = 3 # if you are using Python property
print(cipher.encrypt("hello WORLD!")); # prints "khoor zruog$"
print(cipher.decrypt("KHOOR zruog$")); #prints "hello world!"

cipher.set_key(6);
print(cipher.encrypt("zzz")); #prints "fff"
print(cipher.decrypt("FFF")); #prints "zzz"

cipher.set_key(-6); #Negative keys should be supported!
print(cipher.encrypt("FFF")); #prints "zzz"

class Encryption:
    def __init__(self):
        self.key = 27

    def encrypt(self, data: str) -> str:
        return "".join(chr(ord(c) ^ self.key) for c in data)

    def decrypt(self, data: str) -> str:
        return "".join(chr(ord(c) ^ self.key) for c in data)

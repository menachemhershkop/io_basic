from encreption import Encryption
class Encrept_file(Encryption):
    def encreption(self,massage):
        lowercase_alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        uppercase_alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        print(lowercase_alphabet)
        print(uppercase_alphabet)
        for i in massage:
            if i in lowercase_alphabet or i in uppercase_alphabet:

                with open ("secret.txt","a") as file:
                    file.write(self.encrypt(i))
            with open("secret.txt", "a") as file:
                file.write(self.encrypt(i))
a=Encrept_file()
a.encreption("abc dsd")
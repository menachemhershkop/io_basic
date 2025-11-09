from encreption import Encryption
class File_decrypt(Encryption):
    def decrept_file(self,file):
        with open(file,"r") as defile:
            for i in defile.read():
                print(self.decrypt(i),end="")

a=File_decrypt()
a.decrept_file("secret.txt")

import hashlib

class Md5hashiter:
    def __init__(self, datafile):
        self.datafile=datafile
        self.fd=open(self.datafile,encoding='utf-8')

    def __iter__(self):
        return self

    def __next__(self):
        nextline = self.fd.readline()
        if not nextline:
            self.fd.close()
            raise StopIteration
        hash_object = hashlib.md5(nextline.encode())
        return hash_object
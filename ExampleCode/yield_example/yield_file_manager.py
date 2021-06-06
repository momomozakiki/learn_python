class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.opened_file = open(self.filename)
        return self.opened_file

    def __exit__(self, *exc):
        self.opened_file.close()


with FileManager('readme.txt') as file:
    text = file.read()

file = FileManager('readme.txt')
with file as managed_file:
    text = managed_file.read()
    print(text)


def open_file(filename):
    file = FileManager(filename)
    return file


with open_file('readme.txt') as managed_file:
    text = managed_file.read()
    print(text)
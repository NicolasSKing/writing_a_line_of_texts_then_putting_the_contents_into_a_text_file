class TextFileWriter:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_lines(self):
        file = open(self.file_name, "a")
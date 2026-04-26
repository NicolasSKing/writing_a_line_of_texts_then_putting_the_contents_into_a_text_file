class TextFileWriter:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_lines(self):
        file = open(self.file_name, "a")

        while True:
            user_line = input("Enter a line of text: ")
            file.write(user_line + "\n")
            
from .interfaces.file_saver import FileSaver

class FileSaver(FileSaver):
    def save_to_file(self, art_text, filename):
        with open(filename, "w") as file:
            file.write(art_text)
        print(f"ASCII art has been saved to {filename}")
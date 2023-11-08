from abc import ABC, abstractmethod

class FileSaver(ABC):
    @abstractmethod
    def save_to_file(self, art_text, filename):
        pass
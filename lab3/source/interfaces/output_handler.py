from abc import ABC, abstractmethod
class OutputHandler(ABC):
    @abstractmethod
    def display(self, art_text):
        pass


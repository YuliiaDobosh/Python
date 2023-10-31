from abc import ABC, abstractmethod

class OutputHandler(ABC):
    @abstractmethod
    def display(self, string: str):
        pass
from abc import ABC, abstractmethod
class Program(ABC):
    @abstractmethod
    def run(self):
        pass
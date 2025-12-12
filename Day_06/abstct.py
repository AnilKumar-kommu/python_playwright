from abc import ABC, abstractmethod
class Vichile(ABC):
    def __init__(self,n):
        self.no_of_types = n
    @abstractmethod
    def satrt (self):
        pass

v = Vichile()

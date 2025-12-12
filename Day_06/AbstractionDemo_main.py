from abc import ABC,abstractmethod


class Vichile(ABC):
    def __init__(self,n):
        self.no_of_types = n
    def satrt (self):
        pass
class Bike():
    def __init__(self, n):
        self.no_of_types = n
    def start(self):
        print("Bike start")
class Car():
    def __init__(self, n):
        self.no_of_types = 4
    def start(self):
        print("car start")
class Scooty():
    def __init__(self, n):
        self.no_of_types = 2
    def start(self):
        print("scooty start")
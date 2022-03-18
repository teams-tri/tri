import random as r
from enum import Enum


class DataType(Enum):
    BEST = "Best case",
    AVERAGE = "Average case",
    BAD = "Bad case",

class GenericData():
    def __init__(self, data_type, file_name):
        self.type = data_type
        self.file_name = file_name

    def generate(self, number) -> list:
        pass

class BestCase(GenericData):
    def __init__(self):
        GenericData.__init__(self, DataType.BEST, "files/best_case.txt")

    def generate(self, number):
        return [j for j in range(number)]

class BadCase(GenericData):
    def __init__(self):
        GenericData.__init__(self, DataType.BAD, "files/bad_case.txt")

    def generate(self, number):
        return [j for j in range(number, 0, -1)]

class AverageCase(GenericData):
    def __init__(self):
        GenericData.__init__(self, DataType.AVERAGE, "files/average_case.txt")

    def generate(self, number):
        return [r.randint(0, j) for j in range(number)]


class DataGenerator:

    def __init__(self, max_number):
        self.max_number = max_number

    def _build_case(self, case: GenericData, interval=10):
        with open(case.file_name, "w") as f:
            for i in range(interval, self.max_number, 200):
                f.write((" ".join(map(str, case.generate(i))) + "\n"))

    def process(self):
        self._build_case(BestCase())
        self._build_case(BadCase())
        self._build_case(AverageCase())


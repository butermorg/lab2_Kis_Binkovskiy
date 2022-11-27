import random


class Oms_Policy():
    def __init__(self):
        self.number = []
        self.string_number = ""

    def random_number(self):
        for i in range(4):
            self.part_number = random.randint(1000, 9999)
            self.number.append(self.part_number)
        return self.number

    def form_number(self):
        for item in self.random_number():
            self.string_number += f"{item} "
        return self.string_number

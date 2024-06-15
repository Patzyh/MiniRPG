import random


class Gegner:
    def __init__(self, enemytype=0):
        self.__leben = 100
        self.__enemytype = enemytype
        if self.__enemytype == 0:
            self.__enemytype = random.randint(1, 3)
        self.__dead = False

        self.__enemy = [
            {"name": "Orc", "angriff": 14, "leben": 17},
            {"name": "Goblin", "angriff": 16, "leben": 15},
            {"name": "Geist", "angriff": 18, "leben": 13}
        ]

        self.__enemy = self.__enemy[self.__enemytype - 1]
        self.__name = self.__enemy["name"]

    @property
    def dead(self):
        return self.__dead

    @dead.setter
    def dead(self, dead):
        self.__dead = dead

    @property
    def leben(self):
        return self.__leben

    @leben.setter
    def leben(self, leben):
        self.__leben = leben

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

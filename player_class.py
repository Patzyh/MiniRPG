import random


class Spieler:
    def __init__(self, name, class_type, window):
        self.__name = name
        self.__class_type = class_type
        self.__level = 1
        self.__max_xp = 200
        self.__xp = 0
        self.__ui = window
        self.__class_types = { # haben wir selber gebalanced, sonst wärs legit unmöglich
            "Kämpfer": {"health": 60, "atk": 14},
            "Bogenschütze": {"health": 50, "atk": 17},
            "Magier": {"health": 40, "atk": 20}
        }

        if class_type in self.__class_types:
            self.__health = self.__class_types[class_type]["health"]
            self.__maxhealth = self.__class_types[class_type]["health"]
            self.__atk = self.__class_types[class_type]["atk"]

        # self.__health, self.__maxhealth = 100, 100

    def get_name(self):
        return self.__name

    def get_hp(self):
        return self.__health

    def get_atk(self):
        return self.__atk

    def get_level(self):
        return self.__level

    def get_class(self):
        return self.__class_type


    def set_name(self, name):
        self.__name = name

    def set_hp(self, hp):
        if hp > self.__maxhealth:
            hp = self.__maxhealth
        self.__health = hp
        self.__ui.update_health(hp / self.__maxhealth)

    def set_atk(self, atk):
        self.__atk = atk

    def set_level(self, level):
        self.__level = level
        self.__ui.update_level(level)

    def get_damage(self):
        return self.__atk - random.randint(1,3)
    def get_xp(self):
        return self.__xp
    def get_max_xp(self):
        return self.__max_xp
    def add_xp(self, xp):
        self.__xp += xp
        self.__ui.update_xp(xp / self.__max_xp)
    def update_max_xp(self):
        self.__max_xp += 10 * self.__level -1 # 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300 usw.

    def level_up(self):
        self.__ui.update_level(self.__xp / self.__max_xp)
        if self.__xp >= self.__max_xp:
            self.__level += 1
            self.__xp = self.__xp - self.__max_xp
            self.__ui.update_level(self.__level)
            self.update_max_xp()
            self.__maxhealth += 2
            self.__health = self.__maxhealth
            self.__atk += 1



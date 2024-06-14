from player_class import Spieler
from enemy_class import Gegner
import random

class Spiel:
    def __init__(self, name, class_type, window):
        self.__punkte = 0
        self.__ui = window
        print(type(self.__ui))
        self.__spieler = Spieler(name, class_type, self.__ui)
        self.__rounds = 0
        self.__location = "On the Way to the Dark Forest"

    def spielstand(self):
        print("Punkte: ", self.__punkte)

    def initate_fight(self):
        self.__gegner = Gegner()

    def attack(self):
        self.__gegner.set_leben(self.__gegner.get_leben() - self.__spieler.get_atk())
        if self.__gegner.get_leben() <= 0:
            self.__gegner.set_dead()
            self.__punkte += 1
            self.__gegner = Gegner()
            print("Gegner besiegt")
        else:
            self.__spieler.set_hp(self.__spieler.get_hp() - self.__gegner.get_atk())
            if self.__spieler.get_hp() <= 0:
                print("Spieler besiegt")
                self.stop()

    def get_player(self):
        return self.__spieler


    def stealth_attack(self):
        self.__spieler.set_hp(self.__spieler.get_hp() - self.__gegner.get_atk())
        if self.__spieler.get_hp() <= 0:
            print("Spieler besiegt")
            self.stop()

    def laufen(self):
        self.__rounds += 1
        self.start_next_round()
        if self.__rounds == 5:
            pass


    def the_dark_forest(self):
        print("Du befindest dich im dunklen Wald. Es ist Nacht und du siehst kaum die Hand vor Augen.")
        print("Du hörst Geräusche um dich herum und bist auf der Hut.")
        self.start_next_round()
    def start_next_round(self):
        standard_gegner = random.randint(1, 5)
        stealth = random.randint(1, 20)
        if standard_gegner == 1:
            self.initate_fight()
            print("Ein Gegner ist in der Nähe. Ich sollte mich auf einen Kampf vorbereiten.")
        else:
            print("Es scheint kein Gegner in der Nähe zu sein. Ich kann wohl unbesorgt weitergehen.")
        if stealth == 1:
            print("Ein Gegener greift aus dem Schatten an.")
            self.initate_fight()
            self.stealth_attack()




    def spielende(self):
        self.spielstand()
        print("Spielende")

    def stop(self):
        self.spielende()

    def get_class_type(self):
        return self.__spieler.get_class_type()
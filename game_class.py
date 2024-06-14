from player_class import Spieler
from enemy_class import Gegner
import random
import time

class Spiel:
    def __init__(self, name, class_type, window): # yurr
        self.__punkte = 0
        self.__ui = window
        print(type(self.__ui))
        self.__spieler = Spieler(name, class_type, self.__ui)
        self.__rounds = 0
        self.__location = "Auf dem Weg zum dunkel Wald"

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
            self.__ui.print("Gegner besiegt", 4000)
        else:
            self.__spieler.set_hp(self.__spieler.get_hp() - self.__gegner.get_atk())
            if self.__spieler.get_hp() <= 0:
                self.__ui.print("Spieler besiegt", 4000)
                self.stop()

    def get_player(self):
        return self.__spieler


    def stealth_attack(self):
        self.__spieler.set_hp(self.__spieler.get_hp() - self.__gegner.get_atk())
        if self.__spieler.get_hp() <= 0:
            self.__ui.print("Spieler besiegt",4000)
            self.stop()

    def laufen(self):
        self.__rounds += 1
        self.start_next_round()
        if self.__rounds == 5:
            self.__ui.print("Du befindest dich im dunklen Wald. Es ist Nacht und du siehst kaum die Hand vor Augen.", 6000)
            self.set_location("The Dark Forest")
        elif self.__rounds == 12:
            self.__ui.print("Du befindest dich vor einem alten Schloss. Es ist verlassen und du siehst nur noch die Ruinen.", 6000)
            self.set_location("The Hounted Castle")
        elif self.__rounds == 20:
            self.__ui.print("Du befindest dich vor Malakars Turm. Ein finsterer Ort, an dem böse Mächte wirken.", 6000)
            self.set_location("Malakars Tower")

        if self.__location == "The Dark Forest":
            self.the_dark_forest()
        elif self.__location == "The Hounted Castle":
            self.hounted_castle()
        elif self.__location == "Malakars Tower":
            self.malakars_tower()



    def the_dark_forest(self):
        self.__ui.print("Du hörst Geräusche um dich herum und bist auf der Hut.",4000)
        self.set_location("Auf dem Weg zum Schloss")
        self.start_next_round()

    def hounted_castle(self):
        self.__ui.print("Dir läuft ein kalter Schauer über den Rücken. ", 4000)
        self.set_location("Auf dem Weg zum Turm von Malakar")
        self.start_next_round()

    def malakars_tower(self):
        self.__ui.print("Du spürst die dunkle Aura, die von dem Turm ausgeht.", 4000)
        self.start_next_round()

    def start_next_round(self):
        standard_gegner = random.randint(1, 10)
        stealth = random.randint(1, 20)
        if standard_gegner == 1:
            self.initate_fight()
            self.__ui.print("Ein Gegner ist in der Nähe. Ich sollte mich auf einen Kampf vorbereiten.", 4000)
        else:
            self.__ui.print("Es scheint kein Gegner in der Nähe zu sein. Ich kann wohl unbesorgt weitergehen.",4000)
        if stealth == 1:
            self.__ui.print("Ein Gegener greift aus dem Schatten an.", 4000)
            self.initate_fight()
            self.stealth_attack()



    def get_location(self):
        return self.__location

    def spielende(self):
        self.spielstand()
        print("Spielende")

    def stop(self):
        self.spielende()

    def get_class_type(self):
        return self.__spieler.get_class_type()
    def set_location(self, location):
        self.__location = location
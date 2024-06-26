from player_class import Spieler
from enemy_class import Gegner
import random


class Spiel:
    def __init__(self, name, class_type, window):  # yurr
        self.__ui = window
        self.__spieler = Spieler(name, class_type, self.__ui)
        self.__round = 0
        self.__location = "Auf dem Weg zum dunkel Wald"
        self.__gegner = None

        self.__current_attacker = None


    def initate_fight(self, first_attack, boss=False):
        self.__ui.print("Ein Gegner greift dich an.", 4000)
        if boss:
            self.__gegner = Gegner(4, window=self.__ui)
        else:
            self.__gegner = Gegner(0, window=self.__ui, level=self.__spieler.get_level())
        self.__current_attacker = first_attack

    def next_attack(self):
        if self.__gegner.dead or self.__spieler.get_hp() <= 0:
            self.__current_attacker = None #type shit
            return

        print(self.__current_attacker)
        if self.__current_attacker == "enemy":
            damage = self.__gegner.atk
            self.__spieler.set_hp(self.__spieler.get_hp() - damage)
            self.__ui.print("Du hast " + str(damage) + " Schaden genommen.", 4000)
            if self.__spieler.get_hp() <= 0:
                self.stopfight(False)
            self.__current_attacker = "player"
        else:
            damage = self.__spieler.get_damage()
            self.__gegner.leben = self.__gegner.leben - damage
            self.__ui.print("Du hast " + str(self.__spieler.get_damage()) + " Schaden gemacht.", 4000)
            if self.__gegner.leben <= 0:
                if self.__gegner.name == "Malakar":
                    self.__ui.page_select(6)
                    self.__ui.fancy_print("+ 10.000 Aura.", 4000)
                else:
                    self.__ui.print("+ 1000 Aura", 4000)
                    self.stopfight(True)
            self.__current_attacker = "enemy"

    def stopfight(self, win):
        if win:
            self.__ui.print("Du hast den Kampf gewonnen.", 4000)
            self.__spieler.add_xp(self.__gegner.xp)
            self.__spieler.level_up()
        else:
            self.stop_game()
        self.__gegner.dead = True
        self.__current_attacker = None
        self.__gegner = None  # Setze den Gegner auf None, wenn der Kampf vorbei ist


    def the_dark_forest(self):
        self.__ui.print("Du hörst Geräusche um dich herum und bist auf der Hut.", 4000)
        self.__location = "Auf dem Weg zum Schloss"
        self.start_next_round()

    def hounted_castle(self):
        self.__ui.print("Dir läuft ein kalter Schauer über den Rücken. ", 4000)
        self.__location = "Auf dem Weg zum Turm von Malakar"
        self.start_next_round()

    def malakars_tower(self):
        self.__ui.print("Du spürst die dunkle Aura, die von dem Turm ausgeht.", 4000)
        self.start_next_round()

    def start_next_round(self):
        standard_gegner = random.randint(1, 10)
        stealth = random.randint(1, 20)
        if standard_gegner == 1:
            stealth = 0
            self.initate_fight("player")
            self.__ui.print("Ein Gegner ist in der Nähe. Ich sollte mich auf einen Kampf vorbereiten.", 4000)
        elif standard_gegner == 2 and self.__location == "Malakars dark Tower":
            stealth = 0
            self.initate_fight("player", True)
            self.__ui.fancy_print(" Malakar hat dich entdeckt. Du greifst ihn an.", 6000)
        else:
            self.__ui.print("Es scheint kein Gegner in der Nähe zu sein. Ich kann wohl unbesorgt weitergehen.", 4000)
        if stealth == 1:
            self.__ui.print("Ein Gegener greift aus dem Schatten an.", 4000)
            self.initate_fight("enemy")

    def laufen(self):
        if self.__gegner and not self.__gegner.dead:
            # Wenn ein Kampf im Gange ist, führe den nächsten Angriff aus
            self.next_attack()
        else:
            # Wenn kein Kampf im Gange ist, starte eine neue Runde
            print(self.__round)
            self.__round = self.__round + 1
            self.update_location()
            self.start_next_round()

    def update_location(self):
        if self.__location == "The Dark Forest":
            self.__location = "Auf dem Weg zum Hounted Castle"
        elif self.__location == "Haunted Castle":
            self.__location = "Auf dem Weg zum Haunted Castle"
        elif self.__location == "Haunted Castle":
            self.__location = "Auf dem Weg zum Turm von Malakar"
        if self.__round == 20:
            self.__ui.print("Du befindest dich im dunklen Wald. Es ist Nacht und du siehst kaum die Hand vor Augen.", 6000)
            self.__location = "The Dark Forest"
            # ui current location update
        elif self.__round == 40:
            self.__ui.print("Du befindest dich vor einem alten Schloss. Es ist verlassen und du siehst nur noch die Ruinen.", 6000)
            self.__location = "Haunted Castle"
            # ui current location update
        elif self.__round == 70:
            self.__ui.print("Du befindest dich vor Malakars Turm. Ein finsterer Ort, an dem böse Mächte wirken.", 6000)
            self.__location = "Malakars dark Tower"
        self.__ui.update_location(self.__location)
            # ui current location update

    def stop_game(self):
        self.__ui.page_select(5)

    # Wenn Sie sich das ansehen sollten Sie sich nicht die Getter und Setter ansehen
    # Getter and Setter for ui
    @property
    def ui(self):
        return self.__ui

    @ui.setter
    def ui(self, ui):
        self.__ui = ui

    # Getter and Setter for spieler
    @property
    def spieler(self):
        return self.__spieler

    @spieler.setter
    def spieler(self, spieler):
        self.__spieler = spieler

    # Getter and Setter for round
    @property
    def round(self):
        return self.__round

    @round.setter
    def round(self, temp):
        self.__round = temp

    # Getter and Setter for location
    def get_location(self):
        return self.__location


    def set_location(self, location):
        self.__location = location

    # Getter and Setter for gegner
    @property
    def gegner(self):
        return self.__gegner

    @gegner.setter
    def gegner(self, gegner):
        self.__gegner = gegner

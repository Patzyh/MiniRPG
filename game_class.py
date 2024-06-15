from player_class import Spieler
from enemy_class import Gegner


class Spiel:
    def __init__(self, name, class_type, window):  # yurr
        self.__punkte = 0
        self.__ui = window
        self.__spieler = Spieler(name, class_type, self.__ui)
        self.__round = 0
        self.__location = "Auf dem Weg zum dunkel Wald"
        self.__gegner = None

    def update_location(self):
        if self.__round == 5:
            self.__ui.print("Du befindest dich im dunklen Wald. Es ist Nacht und du siehst kaum die Hand vor Augen.", 6000)
            self.__location = "The Dark Forest"
            # ui current location update
        elif self.__round == 12:
            self.__ui.print("Du befindest dich vor einem alten Schloss. Es ist verlassen und du siehst nur noch die Ruinen.", 6000)
            self.__location = "Hounted Castle"
            # ui current location update
        elif self.__round == 20:
            self.__ui.print("Du befindest dich vor Malakars Turm. Ein finsterer Ort, an dem böse Mächte wirken.", 6000)
            self.__location = "Malakars dark Tower"
            # ui current location update

    def initate_fight(self):
        self.__gegner = Gegner()
        self.__ui.print("Ein " + self.__gegner.name + " greift dich an.", 4000)
        return self.__gegner

    def stop_game(self):
        self.__ui.print("Du hast das Spiel beendet.", 4000)
        self.__ui.print("Du hast " + str(self.__punkte) + " Punkte erreicht.", 4000)
        self.__ui.print("Das Spiel wird beendet.", 4000)
        self.__ui.quit()

    # Getter and Setter for punkte
    @property
    def punkte(self):
        return self.__punkte

    @punkte.setter
    def punkte(self, punkte):
        self.__punkte = punkte

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
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        self.__location = location

    # Getter and Setter for gegner
    @property
    def gegner(self):
        return self.__gegner

    @gegner.setter
    def gegner(self, gegner):
        self.__gegner = gegner

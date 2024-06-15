from player_class import Spieler


class Spiel:
    def __init__(self, name, class_type, window):  # yurr
        self.__punkte = 0
        self.__ui = window
        self.__spieler = Spieler(name, class_type, self.__ui)
        self.__round = 0
        self.__location = "Auf dem Weg zum dunkel Wald"
        self.__gegner = None

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
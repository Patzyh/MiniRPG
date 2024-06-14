import ui_class as ui
from game_class import Spiel

spiel = None


def initiate_game(name, class_type):
    global spiel
    spiel = Spiel(name, class_type)
    class_stats = [spiel.get_player().get_hp()]


def main():
    window = ui.App("v0.0.1 INDEV")
    window.mainloop()


print(__name__)

if __name__ == "__main__":
    main()


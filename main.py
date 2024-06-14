import ui_class as ui
from game_class import Spiel


def initiate_game(name, class_type):
    spiel = Spiel(name, class_type)


def main():
    window = ui.App("v0.0.1 INDEV")
    window.mainloop()

print(__name__)

if __name__ == "__main__":
    main()


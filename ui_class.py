import customtkinter as tk
from tkextrafont import Font
from PIL import Image
import time


class App(tk.CTk):

    __story = ("Du befindest dich im einst strahlenden Land Eldoria, "
                "das nun von einem dunklen Fluch überschattet wird. "
                "Der böse Zauberer Malakar hat das Schattenreich erobert und droht, "
                "die Welt in ewige Nacht zu stürzen. Deine Aufgabe ist es, das Schattenreich zu durchqueren, "
                "gefährliche Gegner zu besiegen und das Licht nach Eldoria zurückzubringen. "
                "Nur du kannst den dunklen Zauberer stoppen und das Land retten. "
                "\n\n――――――――――――――――――――――――――――――――――――"
                "\n\nDas Schicksal Eldorias liegt in deinen Händen. Wirst du es schaffen?")

    def __init__(self, ver: str):
        super().__init__()
        tk.set_default_color_theme("resources/theme/orange.json") # color setter

        self.__fighter = tk.CTkImage(dark_image=Image.open("resources/materials/sword.png"), size=(100, 100))
        self.__archer = tk.CTkImage(dark_image=Image.open("resources/materials/bow-and-arrow.png"), size=(100, 100))
        self.__mage = tk.CTkImage(dark_image=Image.open("resources/materials/magic-wand.png"), size=(100, 100))

        Font(file="resources/fonts/Montserrat-VariableFont_wght.ttf") # font setter
        self.sizeto(600, 400)
        self.title("REALM OF SHADOWS - RPG - " + ver)
        self.page_select(0)

    def page_select(self, page):
        self.clear_site()
        if page == 0:
            self.label = tk.CTkLabel(self, text="REALM OF SHADOWS", font=("Montserrat Black", 40))
            self.label.pack(pady=10)

            self.description = tk.CTkLabel(self, text=self.__story, font=("Montserrat", 15),
                                           justify="center", anchor="n", wraplength=600)
            self.description.pack(pady=30, padx=0)

            self.button = tk.CTkButton(self, text="Starten", font=("Montserrat Black", 20, "bold"), command=lambda: self.page_select(1))
            self.button.pack(pady=10, side="bottom")
        elif page == 1:
            self.label = tk.CTkLabel(self, text="ROLE SELECT", font=("Montserrat Black", 40))
            self.label.pack(pady=10)

            self.fighter = tk.CTkButton(self, text="Kämpfer", font=("Montserrat Black", 20, "bold"), image=self.__fighter, compound="top", command=lambda: self.selected_role(1), fg_color="transparent", hover_color=("#ff0000", "#424242"))
            self.fighter.pack(padx=23, pady=70, side="left", anchor="n")

            self.archer = tk.CTkButton(self, text="Bogenschütze", font=("Montserrat Black", 20, "bold"), image=self.__archer, compound="top", command=lambda: self.selected_role(2), fg_color="transparent", hover_color=("#ff0000", "#424242"))
            self.archer.pack(padx=23, pady=70, side="left", anchor="n")

            self.mage = tk.CTkButton(self, text="Magier", font=("Montserrat Black", 20, "bold"), image=self.__mage, compound="top", command=lambda: self.selected_role(3), fg_color="transparent", hover_color=("#ff0000", "#424242"))
            self.mage.pack(padx=23, pady=70, side="left", anchor="n")

            self.button = tk.CTkButton(self, text="Zurück", font=("Montserrat Black", 20, "bold"), command=lambda: self.page_select(0))
            self.button.place(x=10, y=360)
        elif page == 2:
            self.label = tk.CTkLabel(self, text=self.__role.upper(), font=("Montserrat Black", 40))
            self.label.pack(pady=10)

            self.description = tk.CTkLabel(self,
                                           text="Du hast die Rolle"
                                                " " + self.__role + " ausgewählt."
                                                "\n\n――――――――――――――――――――――――――――――――――――"
                                                "\n\nBist du dir mit dieser Rolle sicher?",
                                           font=("Montserrat", 15), justify="center", anchor="n", wraplength=600)
            self.description.pack(pady=50, padx=0)

            self.button = tk.CTkButton(self, text="Weiter", font=("Montserrat Black", 20, "bold"), command=lambda: self.page_select(3))
            self.button.pack(pady=5, padx=5, side="bottom", anchor="e")

            self.button = tk.CTkButton(self, text="Zurück", font=("Montserrat Black", 20, "bold"), command=lambda: self.page_select(1))
            self.button.place(x=10, y=360)
        elif page == 3:
            self.level = tk.CTkProgressBar(self, width=15, height=250, orientation="vertical", progress_color="#3498db", mode="determinate", determinate_speed=0.2)
            self.level.place(x=565, y=75)

            self.levellabel = tk.CTkLabel(self, text="XP", font=("Montserrat Black", 20), bg_color="transparent")
            self.levellabel.place(x=557, y=45)

            self.levelnum = tk.CTkLabel(self, text="10", font=("Montserrat Black", 20), bg_color="transparent", anchor="center")
            self.levelnum.place(x=565, y=330)

            # make level go full and clear it to test
            self.level.start()

            self.health = tk.CTkProgressBar(self, width=250, height=15, progress_color="#2ecc71", mode="determinate", determinate_speed=0.2, orientation="horizontal")
            self.health.place(x=200, y=370)

            self.healthlabel = tk.CTkLabel(self, text="HP", font=("Montserrat Black", 20), bg_color="transparent")
            self.healthlabel.place(x=160, y=362)



    def initiate_game(self):
        pass
    def selected_role(self, num):
        self.__role = ""
        if num == 1:
            self.__role = "Kämpfer"
        elif num == 2:
            self.__role = "Bogenschütze"
        elif num == 3:
            self.__role = "Magier"
        self.page_select(2)

    def on_button_click(self):
        self.label.configure(text="Button clicked!")

    def clear_site(self):
        for widget in self.winfo_children():
            widget.destroy()

    def sizeto(self, width, height):
        self.maxsize(width, height)
        self.minsize(width, height)
        self.geometry(f"{width}x{height}")



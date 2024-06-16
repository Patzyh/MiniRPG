import customtkinter as tk
from tkextrafont import Font
import pygame
from PIL import Image
import main


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
        tk.set_appearance_mode("dark")
        self.__fighter = tk.CTkImage(dark_image=Image.open("resources/materials/sword.png"), size=(100, 100))
        self.__archer = tk.CTkImage(dark_image=Image.open("resources/materials/bow-and-arrow.png"), size=(100, 100))
        self.__mage = tk.CTkImage(dark_image=Image.open("resources/materials/magic-wand.png"), size=(100, 100))
        self.__kevin = tk.CTkImage(dark_image=Image.open("resources/materials/Kevinxmarkus.png"), size=(800, 400))
        self.__healpot = tk.CTkImage(dark_image=Image.open("resources/materials/healpot.png"), size=(50, 50))
        self.__healpot_gray = tk.CTkImage(dark_image=Image.open("resources/materials/healpot_gray.png"), size=(50, 50))

        self.__player = None
        self.__game_logic = None

        Font(file="resources/fonts/Montserrat-VariableFont_wght.ttf") # font setter
        self.sizeto(600, 400)
        self.title("REALM OF SHADOWS - RPG - " + ver)
        self.page_select(0)
        self.__konami_code = ['Up', 'Up', 'Down', 'Down', 'Left', 'Right', 'Left', 'Right', 'b', 'a']
        self.__key_presses = []

        self.bind('<KeyPress>', self.check_konami_code)

    def check_konami_code(self, event):
        if event.keysym == self.__konami_code[len(self.__key_presses)]:
            self.__key_presses.append(event.keysym)
            if self.__key_presses == self.__konami_code:
                self.__kevin_label = tk.CTkLabel(self, image=self.__kevin, text="")
                self.__kevin_label.place(x=0, y=0)
                self.after(5000, self.__kevin_label.destroy)
                self.__key_presses = []
        else:
            self.__key_presses = []

    def page_select(self, page):
        self.clear_site()
        if page == 0:
            self.__label = tk.CTkLabel(self, text="REALM OF SHADOWS", font=("Montserrat Black", 40))
            self.__label.pack(pady=10)

            self.__description = tk.CTkLabel(self, text=self.__story, font=("Montserrat", 15),
                                           justify="center", anchor="n", wraplength=600)
            self.__description.pack(pady=30, padx=0)

            self.__button = tk.CTkButton(self, text="Starten", font=("Montserrat Black", 20, "bold"), command=lambda: self.page_select(1))
            self.__button.pack(pady=10, side="bottom")
        elif page == 1:
            self.__label = tk.CTkLabel(self, text="CHARAKTERERSTELLUNG", font=("Montserrat Black", 40))
            self.__label.pack(pady=10)

            self.__name = tk.CTkEntry(self, font=("Montserrat", 15), placeholder_text="Geb hier deinen Namen ein:", height=30, width=300)
            self.__name.pack(pady=70)

            self.__button = tk.CTkButton(self, text="Weiter", font=("Montserrat Black", 20, "bold"), command=self.save_name)
            self.__button.pack(pady=10, side="bottom")
        elif page == 2:
            self.__label = tk.CTkLabel(self, text="WÄHLE DEINE ROLLE", font=("Montserrat Black", 40))
            self.__label.pack(pady=10)

            self.__fighterbtn = tk.CTkButton(self, text="Kämpfer", font=("Montserrat Black", 20, "bold"), image=self.__fighter, compound="top", command=lambda: self.selected_role(1), fg_color="transparent", hover_color=("#ff0000", "#424242"))
            self.__fighterbtn.pack(padx=23, pady=70, side="left", anchor="n")

            self.__archerbtn = tk.CTkButton(self, text="Bogenschütze", font=("Montserrat Black", 20, "bold"), image=self.__archer, compound="top", command=lambda: self.selected_role(2), fg_color="transparent", hover_color=("#ff0000", "#424242"))
            self.__archerbtn.pack(padx=23, pady=70, side="left", anchor="n")

            self.__magebtn = tk.CTkButton(self, text="Magier", font=("Montserrat Black", 20, "bold"), image=self.__mage, compound="top", command=lambda: self.selected_role(3), fg_color="transparent", hover_color=("#ff0000", "#424242"))
            self.__magebtn.pack(padx=23, pady=70, side="left", anchor="n")

            self.__buttonbtn = tk.CTkButton(self, text="Zurück", font=("Montserrat Black", 20, "bold"), command=lambda: self.page_select(0))
            self.__buttonbtn.place(x=10, y=360)
        elif page == 3:
            self.__label = tk.CTkLabel(self, text=self.__role.upper(), font=("Montserrat Black", 40))
            self.__label.pack(pady=10)

            self.__description = tk.CTkLabel(self,
                                           text="Du hast die Rolle"
                                                " " + self.__role + " ausgewählt."
                                                "\n\n――――――――――――――――――――――――――――――――――――"
                                                "\n\nBist du dir mit dieser Rolle sicher?",
                                           font=("Montserrat", 15), justify="center", anchor="n", wraplength=600)
            self.__description.pack(pady=50, padx=0)

            self.__button = tk.CTkButton(self, text="Weiter", font=("Montserrat Black", 20, "bold"), command=lambda: self.page_select(4))
            self.__button.pack(pady=5, padx=5, side="bottom", anchor="e")

            self.__button = tk.CTkButton(self, text="Zurück", font=("Montserrat Black", 20, "bold"), command=lambda: self.page_select(2))
            self.__button.place(x=10, y=360)
        elif page == 4:
            self.__level = tk.CTkProgressBar(self, width=15, height=250, orientation="vertical", progress_color="#3498db", mode="determinate", determinate_speed=0.2)
            self.__level.place(x=565, y=75)

            self.__levellabel = tk.CTkLabel(self, text="XP", font=("Montserrat Black", 20), bg_color="transparent")
            self.__levellabel.place(x=557, y=45)

            self.__levelnum = tk.CTkLabel(self, text="10", font=("Montserrat Black", 20), bg_color="transparent", anchor="center")
            self.__levelnum.place(x=565, y=330)

            self.__level.set(0)

            self.__health = tk.CTkProgressBar(self, width=250, height=15, progress_color="#2ecc71", mode="determinate", determinate_speed=0.2, orientation="horizontal")
            self.__health.place(x=180, y=370)

            self.__health.set(1)

            self.__healthlabel = tk.CTkLabel(self, text="HP", font=("Montserrat Black", 20), bg_color="transparent")
            self.__healthlabel.place(x=140, y=362)

            # self.__debugbutton = tk.CTkButton(self, text="DEBUG", font=("Montserrat Black", 20, "bold"), command=lambda: self.print("Du bist ein hässliches stück scheiße ich muss eigentlich nur den Text von Angelo ersetzen aber was soll ich machen. HERE I AM ON THE ROAD AGAIN. HERE WE ARE NOW ENTERTAIN US.", 4000))
            # self.__debugbutton.place(x=300, y=250)

            self.__move = tk.CTkButton(self, text="Weiter", font=("Montserrat Black", 20, "bold"), command=self.move)
            self.__move.pack(pady=(10, 50), side="bottom")

            self.__healpot_1 = tk.CTkButton(self, image=self.__healpot, text="", bg_color="transparent", command=lambda: self.use_healpot(1), width=20, height=20, fg_color="transparent", hover_color=("#ff0000", "#424242"))
            self.__healpot_1.place(x=10, y=100)

            self.__healpot_2 = tk.CTkButton(self, image=self.__healpot, text="", bg_color="transparent", command=lambda: self.use_healpot(2), width=20, height=20, fg_color="transparent", hover_color=("#ff0000", "#424242"))
            self.__healpot_2.place(x=10, y=160)

            self.__healpot_3 = tk.CTkButton(self, image=self.__healpot, text="", bg_color="transparent", command=lambda: self.use_healpot(3), width=20, height=20, fg_color="transparent", hover_color=("#ff0000", "#424242"))
            self.__healpot_3.place(x=10, y=220)


            main.initiate_game(self.__name, self.__role, self)


    def get_player(self, player):
        self.__player = player

    def use_healpot(self, id):
        print(self.print("Du hast einen Heiltrank benutzt.", 2000))
        if self.__player is not None:
            self.__player.set_hp(999)

            if id == 1:
                # make the button grey and not clickable
                self.__healpot_1.configure(state="disabled", image=self.__healpot_gray)
            elif id == 2:
                # make the button grey and not clickable
                self.__healpot_2.configure(state="disabled", image=self.__healpot_gray)
            elif id == 3:
                # make the button grey and not clickable
                self.__healpot_3.configure(state="disabled", image=self.__healpot_gray)

    def create_enemybar(self, enemy):
        self.__enemyhealth = tk.CTkProgressBar(self, width=250, height=15, progress_color="#e74c3c", mode="determinate", determinate_speed=0.2, orientation="horizontal")
        self.__enemyhealth.place(x=180, y=20)

        self.__enemylabel = tk.CTkLabel(self, text=enemy.name, font=("Montserrat Black", 20), bg_color="transparent")
        self.__enemylabel.pack(pady=(40, 0), padx=0)

        self.__enemyhealth.set(1)

        self.__enemyhealthlabel = tk.CTkLabel(self, text="HP", font=("Montserrat Black", 20), bg_color="transparent")
        self.__enemyhealthlabel.place(x=140, y=12)

    def update_enemybar(self, health: float):
        self.__enemyhealth.set(health)

    def remove_enemybar(self):
        self.__enemyhealth.destroy()
        self.__enemyhealthlabel.destroy()
        self.__enemylabel.destroy()

    def get_gamelogic(self, gamelogic):
        self.__game_logic = gamelogic

    def move(self):
        print(self.__game_logic)

        if self.__game_logic is not None:
            self.__game_logic.laufen()

    def print(self, text, time):
        self.__infolabel = tk.CTkLabel(self, text=text, font=("Montserrat", 15), justify="center", anchor="s",
                                       wraplength=400)
        self.__infolabel.pack(pady=0, padx=50, side="bottom")
        self.after(time, self.__infolabel.destroy)

    def play_title_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load("resources/sounds/blind_pick_music.mp3")
        pygame.mixer.music.play()

    def play_game_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load("resources/sounds/background_music.mp3")
        pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()

    def update_health(self, health: float):
        self.__health.set(health)

    def update_level(self, level: float):
        self.__level.set(level)

    def save_name(self):
        self.__name = self.__name.get()
        self.page_select(2)

    def selected_role(self, num):
        self.__role = ""
        if num == 1:
            self.__role = "Kämpfer"
        elif num == 2:
            self.__role = "Bogenschütze"
        elif num == 3:
            self.__role = "Magier"
        self.page_select(3)

    def on_button_click(self):
        self.__label.configure(text="Button clicked!")

    def clear_site(self):
        for widget in self.winfo_children():
            widget.destroy()

    def sizeto(self, width, height):
        self.maxsize(width, height)
        self.minsize(width, height)
        self.geometry(f"{width}x{height}")



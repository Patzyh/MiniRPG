import customtkinter as tk
from tkextrafont import Font


class App(tk.CTk):
    def __init__(self):
        super().__init__()
        tk.set_default_color_theme("resources/theme/orange.json")
        font = Font(file="resources/fonts/Montserrat-VariableFont_wght.ttf")
        self.sizeto(600, 400)
        self.title("Hello World!")
        self.page_select(0)

    def page_select(self, page):
        self.clear_site()
        if page == 0:
            self.label = tk.CTkLabel(self, text='VOCAB', font=("LEMON MILK Bold", 25))
            self.label.pack(pady=10)

            self.description = tk.CTkLabel(self, text='A simple vocabulary learning tool', font=("Montserrat Black", 15))
            self.description.pack(pady=100, padx=0)

            self.button = tk.CTkButton(self, text='Go', font=("Montserrat Black", 20, "bold"), command=lambda: self.page_select(1))
            self.button.pack(pady=10, side="bottom")

    def on_button_click(self):
        self.label.configure(text='Button clicked!')

    def clear_site(self):
        for widget in self.winfo_children():
            widget.destroy()

    def sizeto(self, width, height):
        self.maxsize(width, height)
        self.minsize(width, height)
        self.geometry(f"{width}x{height}")



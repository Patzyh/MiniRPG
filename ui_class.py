import customtkinter as tk


class App(tk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x150")
        self.title("Hello World!")

        self.label = tk.CTkLabel(self, text='Hello, World!')
        self.label.pack()

        self.button = tk.CTkButton(self, text='Click me!', command=self.on_button_click)
        self.button.pack()

    def on_button_click(self):
        self.label.configure(text='Button clicked!')



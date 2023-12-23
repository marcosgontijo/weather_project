import customtkinter as ctk
from api.api_client import get_weather_data
from data.database import Database
from datetime import datetime

window = ctk.CTk()

class Application():
    def __init__(self):
        self.window = window
        self.tela()
        self.window.mainloop()
    def tela(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.window.geometry("600x400")
        self.window.title("Weather Project")

        self.window.resizable(width=False, height=False)
        self.weather_frame = ctk.CTkFrame(master=window, width=350, height=396)

        self.label = ctk.CTkLabel(self.window, text="* Weather Systems *", text_color="orange", font=("Roboto", 20))
        self.label.place(x=200, y=7)

        self.weather_entry = ctk.CTkEntry(
            master=window,
            placeholder_text="City",
            width=200,
            font=("Roboto", 14))
        self.weather_entry.place(x=25, y=105)

        self.weather_entry_information = ctk.CTkLabel(
            master=self.window, text="* Insira uma cidade para ver a previsão do tempo.",
            text_color="orange",
            font=("Roboto", 12)).place(x=25, y=70)

        self.search_button = ctk.CTkButton(
            master=self.window,
            text="Buscar",
            text_color=("white"),
            width=145,
            fg_color="green",
            command=self.update_weather_data,
            hover_color="#F94620").place(x=250, y=105)

    def update_weather_data(self):
        cidade = self.weather_entry.get()
        temperatura, descricao = get_weather_data(cidade)

        database = Database()

        data = {
                "city": cidade,
                "descrption": descricao,
                "temperature": temperatura,
                "date": datetime.now()
            }

        database.conn_database(data)


Application()

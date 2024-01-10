from tkinter import PhotoImage

import pymongo
import customtkinter as ctk
from api.api_client import get_weather_data
from datetime import datetime
from images import *

from data.database import Database

window = ctk.CTk()

class Application():

    def inicia_db(self):
        mongo_uri = "mongodb+srv://admin:admin@cluster0.tkho3ux.mongodb.net/"
        client = pymongo.MongoClient(mongo_uri)
        database_name = "master"
        return database_name

    def __init__(self):
        db = self.inicia_db()

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

    def info_weahter_city(self, cidade, temperatura, descricao, data):

        datetimenow = datetime.today().strftime('%Y-%m-%d')

        self.weather_entry_city = ctk.CTkLabel(
            master=self.window, text=self.cidade.upper(),
            text_color="white",
            font=("Roboto", 14)).place(x=250, y=180)

        self.weather_entry_temperature = ctk.CTkLabel(
            master=self.window, text=self.temperatura,
            text_color="white",
            font=("Roboto", 14)).place(x=250, y=220)

        self.weather_entry_description = ctk.CTkLabel(
            master=self.window, text=self.descricao,
            text_color="white",
            font=("Roboto", 14)).place(x=250, y=260)

        self.weather_entry_date = ctk.CTkLabel(
            master=self.window, text=datetimenow,
            text_color="white",
            font=("Roboto", 14)).place(x=250, y=300)

        self.img = PhotoImage(file="E:\Projetos\Python\WeatherProject\cloud.png")

        self.label_img = ctk.CTkLabel(
            master=self.window,
            image=self.img,
            text="").place(x=90, y=180)


    def update_weather_data(self):
        self.cidade = self.weather_entry.get()
        self.temperatura, self.descricao = get_weather_data(self.cidade)

        database = Database()

        self.data = {
                "city": self.cidade,
                "temperature": self.temperatura,
                "descrption": self.descricao,
                "date": datetime.now()
            }

        self.info_weahter_city(self.cidade, self.temperatura, self.descricao, datetime.now)

        database.insert_data_mongo(self.data)

Application()

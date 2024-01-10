from _ast import mod

import pymongo
from pymongo import MongoClient


class Database():
    # def innit_bd(self):
    #     mongo_uri = "mongodb+srv://admin:admin@cluster0.tkho3ux.mongodb.net/"
    #     client = pymongo.MongoClient(mongo_uri)
    #     database_name = "master"
    #     db = client[database_name]
    #     #collection_name = "weather"
    #     collection = "weather"

        #resultado = collection.insert_one(dados)

    def insert_data_mongo(self, dados):
        mongo_uri = "mongodb+srv://admin:admin@cluster0.tkho3ux.mongodb.net/"
        client = MongoClient(mongo_uri)

        database_name = "master"
        # Selecionar o banco de dados desejado
        db = client[database_name]

        collection_name = "weather"
        # Selecionar a coleção desejada
        collection = db[collection_name]

        # Inserir dados na coleção
        resultado = collection.insert_one(dados)

        # Retornar o ID do documento recém-inserido
        return resultado.inserted_id











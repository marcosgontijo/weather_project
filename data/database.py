import pymongo

class Database:
    def conn_database(self, dados):
        mongo_uri = "mongodb+srv://admin:admin@cluster0.tkho3ux.mongodb.net/"
        client = pymongo.MongoClient(mongo_uri)

        database_name = "master"
        self.db = client[database_name]

        collection_name = "weather"
        collection = self.db[collection_name]

        print("Banco de dados conectado com sucesso!")

        resultado = collection.insert_one(dados)






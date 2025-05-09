# class Example:
#     def __init__(self, name:str, version:str):
#         self.name = name
#         self.version = version
        

# import json

# with open("config.json","r") as file:
#     my_config: dict = json.load(file)
#     print(my_config["features"])

#     json.dump(file,file)

import json

file = open("LEZIONE_15/config_new.json","w")

db:dict = {
        "GRGFLV...":{"name": "Giorgio", "surname": "Fiorentino", "age":30},
        "TRXMSE...": {"name": "Giovanni","surname": "Fiorentino", "age":20}
}

json.dump(db,file, indent = 4)


file.close()

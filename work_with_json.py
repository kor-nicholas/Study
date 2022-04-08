import json

# Сериализация (из объекта в json)
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file, indent=4, ensure_ascii=False) # сохранить json в файл
#-------------------------------------------------------------------------------------------------------------

json_string = json.dumps(data) # можно работать с данными как со строкой
#-------------------------------------------------------------------------------------------------------------

# Десериализация (из json в объект)
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
#-------------------------------------------------------------------------------------------------------------

json_string_1 = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""

data_1 = json.loads(json_string)
#-------------------------------------------------------------------------------------------------------------







import requests

class Pokemon:
    def __init__(self, name, id, weight, height, stats, type):
        self.name = name
        self.id = id
        self.weight = weight
        self.height = height
        # hp, atk, def, spa, spd, spe
        self.stats = stats
        self.type = type

    def __str__(self):
        outputString = ""
        outputString += f"Name: {self.name.capitalize()} \n"
        outputString += f"ID: {str(self.id)} \n"
        outputString += f"Height: {self.height/10}m, Weight: {self.weight/10}kg \n"
        outputString += f"HP: {self.stats[0]}, Atk: {self.stats[1]}, Def: {self.stats[2]}, SpA: {self.stats[3]}, SpD: {self.stats[4]}, Spe: {self.stats[5]} \n"
        outputString += f"Types: {str(self.type).capitalize()} \n"
        return outputString


r = requests.get("https://www.pokeapi.co/api/v2/pokemon?limit=151")

data = r.json()
results = data["results"]

for result in results[:10]:
    r = requests.get(result["url"])
    data = r.json()

    stats = []
    for stat in data["stats"]:
        stats.append(stat["base_stat"])

    types = []
    for pokeType in data["types"]:
        types.append(pokeType["type"]["name"])

    pokemon = Pokemon(data["name"], data["id"], data["weight"], data["height"], stats, types)
    print(pokemon)
import requests
import json

#json takes the form of a dictionary

pokemon = {
    "name": "Pikachu",
    "type": "electric",
    "base_experience": 112
}

print(pokemon['base_experience'])

response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
# json_data = response.text

# poke_data = json.loads(json_data)
poke_data = response.json()
# print(poke_data)
print(poke_data["name"])
print(poke_data["sprites"]["other"]["dream_world"]["front_default"])
print(poke_data['types'][0]['type']['name'])
print(poke_data['id'])

def pokemon(pokename):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokename}")

    if response.status_code == 200:
        poke_data = response.json()

        poke_dict = {
            "id": poke_data['id'],
            "name": poke_data['name'],
            "type": poke_data['types'][0]['type']['name'],
            "sprite": poke_data["sprites"]["other"]["dream_world"]["front_default"],
        }

        return poke_dict
    else:
        print('Bad Response Try Again')


def poke_hunt():

    while True:
        poke = input('Enter a Pokename or quit: ')
        if poke == 'quit':
            print('You stink!')
            break
        else:
            print(pokemon(poke))

poke_hunt()
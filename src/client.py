import requests
from .models.pokemon import Pokemon
from .models.generation import Generation

class PokeAPIClient:
    BASE_URL = "https://pokeapi.co/api/v2/"

    def __init__(self):
        self.session = requests.Session()

    def get(self, endpoint, params=None):
        url = self.BASE_URL + endpoint
        response = self.session.get(url, params=params)
        response.raise_for_status()
        # except requests.exceptions.HTTPError as errh:
        #     print ("Http Error: ",errh)
        # except requests.exceptions.RequestException as err:
        #     print ("Error: ", err)

        return response.json()

    def get_pokemon(self, id_or_name):
        data = self.get(f"pokemon/{id_or_name}")
        return Pokemon(data)

    def get_generation(self, id_or_name):
        data = self.get(f"generation/{id_or_name}")
        return Generation(data)

    def get_paginated_results(self, endpoint, limit, offset):
        # If omitted, limit defaults to 20
        params = {"limit": limit, "offset": offset}
        return self.get(endpoint, params=params)


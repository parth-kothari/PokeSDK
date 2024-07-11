from .client import PokeAPIClient
from .pokemon_client import Pokemon
from .generation_client import Generation

class PokeAPI:
    def __init__(self):
        self.client = PokeAPIClient()
        self.pokemon = Pokemon(self.client)
        self.generation = Generation(self.client)
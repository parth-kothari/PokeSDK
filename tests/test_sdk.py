import unittest
from src import PokeAPI
from src.models.pokemon import Pokemon
from src.models.paginated_list import PaginatedList

class TestPokemon(unittest.TestCase):
    def setUp(self):
        self.api = PokeAPI()

    def test_get_pokemon_by_id(self):
        pokemon = self.api.pokemon.getByID(1)
        self.assertEqual(pokemon.name, 'bulbasaur')

    def test_get_pokemon_by_name(self):
        pokemon = self.api.pokemon.getByName('pikachu')
        self.assertEqual(pokemon.id, 25)

    def test_get_nonexistent_pokemon(self):
        with self.assertRaises(Exception): 
            self.api.pokemon.getByName('fake-pokemon')

    def test_list_pokemon(self):
        pokemon_list = self.api.pokemon.list(limit=10, offset=0)
        self.assertEqual(len(pokemon_list), 10)

    def test_list_pokemon_with_offset(self):
        pokemon_list = self.api.pokemon.list(limit=10, offset=20)
        self.assertEqual(len(pokemon_list), 10)

class TestGeneration(unittest.TestCase):
    def setUp(self):
        self.api = PokeAPI()

    def test_get_generation_by_id(self):
        generation = self.api.generation.getByID(1)
        self.assertEqual(generation.name, 'generation-i')

    def test_get_generation_by_name(self):
        generation = self.api.generation.getByName('generation-ii')
        self.assertEqual(generation.id, 2)

    def test_list_generations(self):
        generation_list = self.api.generation.list(limit=10, offset=0)
        self.assertGreater(len(generation_list.results), 0)

if __name__ == '__main__':
    unittest.main()
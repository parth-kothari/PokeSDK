from src.models.paginated_list import PaginatedList

class Pokemon:
    POKEMON_ENDPOINT = "pokemon"

    def __init__(self, client):
        self.client = client

    def getByID(self, id):
        # Ran out of time to fix this, but should be checking if a number is passed in
        # if id.instanceOf():
        #     raise Exception("Fetching pokemon by ID must take in a numeric digit")
        return self.client.get_pokemon(id)

    def getByName(self, name):
        # if id.isdigit():
        #     raise Exception("Fetching pokemon by Name must take in a non numeric string")
        return self.client.get_pokemon(name)

    def list(self, limit=20, offset=0):
        data = self.client.get_paginated_results("pokemon", limit, offset)   
        pokemon_list = []
        
        for pokemon_data in data['results']:
            # Get the full data for each generation
            complete_pokemon_data = self.getByName(pokemon_data['name'])
            
            # Create a Generation object and add it to the list
            pokemon_object = Pokemon(complete_pokemon_data)
            pokemon_list.append(pokemon_object)
        
        # Replace the original results with the list of Generation objects
        
        return PaginatedList(
            count=data['count'],
            next_url=data['next'],
            previous_url=data['previous'],
            results=pokemon_list
        )

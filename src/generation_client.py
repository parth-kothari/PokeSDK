from src.models.paginated_list import PaginatedList

class Generation:
    def __init__(self, client):
        self.client = client

    def getByID(self, id):
        return self.client.get_generation(id)
    
    def getByName(self, name):
        return self.client.get_generation(name)

    def list(self, limit, offset):
        data = self.client.get_paginated_results("generation", limit, offset)
        generation_list = []
        
        for generation_data in data['results']:
            # Get the full data for each generation
            complete_generation_data = self.getByName(generation_data['name'])
            
            # Create a Generation object and add it to the list
            generation_object = Generation(complete_generation_data)
            generation_list.append(generation_object)
        
        return PaginatedList(
            count=data['count'],
            next_url=data['next'],
            previous_url=data['previous'],
            results=generation_list
        )

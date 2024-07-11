class Pokemon:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        # TODO: More Fields

    def __repr__(self):
        return f"<Pokemon(id={self.id}, name='{self.name}')>"


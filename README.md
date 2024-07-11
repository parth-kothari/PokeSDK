## Installation
Download this code and run:
cd pokeapi-sdk
pip install 


## How To Use
This SDK provides an abstraction over the PokeAPI for getting and listing pokemon and generations.
To use this, please install the sdk and create a new `PokeAPI` object.

Then, you may use any of the following methods:
- pokeApi.pokemon.getByID
- pokeApi.pokemon.getByName
- pokeApi.generation.getByID
- pokeApi.generation.getByName
- pokeApi.pokemon.list
- pokeApi.generation.list

to run tests, please use `python -m unittest discover tests` when inside the repo

## Design Decisions
Going into this project, I wanted to make the PokeAPI as easy as possible to use and provide
abstractions for users for the API itself.
What this means was creating easy to use models for Pokemon and Generation objects, as well as 
providing a standard PaginatedList object to handle listing either Pokemon or Generations.

Additionally, the API itself lets you pass either an ID or a Name into the pokemon call, I wanted 
to make this safer, so I introduced separate methods for fetching by ID or Name. The intention is to
validate the inputs to those methods, but I had to step away before finishing that up.
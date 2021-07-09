from .pokemon import Pokemon


class Trainer:

    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon_to_add: Pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        self.pokemons.append(pokemon)
        return "Caught " + Pokemon.pokemon_details(pokemon_to_add)

    def release_pokemon(self, pokemon_name: str):
        for p in self.pokemons:
            if pokemon_name == p.name:
                self.pokemons.remove(p)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        pokemon_details = [f'- {Pokemon.pokemon_details(p)}' for p in self.pokemons]
        output = f"Pokemon Trainer {self.name}" + "\n" + f"Pokemon count {len(self.pokemons)}" + "\n"
        return output + '\n'.join(pokemon_details)


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())

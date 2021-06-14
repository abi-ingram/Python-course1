#1a
pokemon = ["Bulbasaur", "Mewtwo", "Gengar", "Magikarp", "Entei"]
print(pokemon)

pokemon.append("Togepi")
print(pokemon)

pokemon.remove("Magikarp")
print(pokemon)

pokemon.pop(2)
print(pokemon)

print(pokemon[2])

#1b
my_team = ["Landorus", "Weedle", "Spearow", "Pidgey", "Gardevoir"]

#1c
pokedex = pokemon + my_team
print(pokedex)

#1d
pokedex.insert(3, "Rattatta")
print(pokedex)

print(len(pokedex))

for item in pokedex:
    print(item)

#3
if "Charizard" in pokedex:
    print("Yes")
else:
    print("No")
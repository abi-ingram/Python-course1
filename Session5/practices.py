pokemon = ["pikachu", "squirtle", "charizard", "snorlax"]
print(pokemon[1])

pokemon[1] = "bulbasaur"
print(pokemon)

pokemon.insert(0, "squirtle")
print(pokemon)

pokemon.append("eevee")
print(pokemon)

#pokemon = pokemon + ["Spongebob", "Squarepants"]
#print(pokemon)

#pokemon = pokemon * 2
#print(pokemon)

#pokemon.remove("charizard")

#pokemon.pop(2)
#print(pokemon)

pokemon.sort()
print(pokemon)

#pokemon_sliced = pokemon[1:3]
#print(pokemon_sliced)

if "pikachu" in pokemon:
    print ("Yes")
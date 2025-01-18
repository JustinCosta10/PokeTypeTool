import pypokedex
import json

def get_pokemon(input_name_or_dex):
    try:
        found_pokemon = pypokedex.get(name=input_name_or_dex)
        if found_pokemon:
            print(f"Name: {found_pokemon.name.capitalize()}")
            print(f"Type(s): {', '.join(found_pokemon.types)}")
            print(f"Pokedex ID: {found_pokemon.dex}")
            print(f"Pokemon Sprite: {found_pokemon.sprites.front.get('default')}")
            return found_pokemon
    except Exception as e:
        print(f"Pokemon not found.")

#Will be used if future features require locally stored data
def get_all_pokemon_data():
    pokemon_list = []
    current_id = 1
    while current_id <= 1025:
        try:
            # Fetch Pokémon by dex ID
            current_pokemon = pypokedex.get(dex=current_id)
            print(f"Found Pokémon {current_id}: {current_pokemon.name}")

            # Create a dictionary for the Pokémon's data
            pokemon_data = {
                "id": current_pokemon.dex,
                "name": current_pokemon.name,
                "types": current_pokemon.types,
                "base_stats": current_pokemon.base_stats,
                "abilities": current_pokemon.abilities,
                #"moves": current_pokemon.moves,
            }
            pokemon_list.append(pokemon_data)
            current_id += 1  # Move to the next dex ID
        except ValueError:
            print("Invalid dex ID. No more Pokémon found.")
            break

    # Save the data to a JSON file
    with open("pokemon_data.json", "w") as json_file:
        json.dump(pokemon_list, json_file, indent=4)
        print("Saved Pokémon data to 'pokemon_data.json'.")

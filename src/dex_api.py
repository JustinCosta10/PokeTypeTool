import pypokedex

def get_pokemon(input_name_or_dex):
    try:
        found_pokemon = pypokedex.get(name=input_name_or_dex)
        if found_pokemon:
            print(f"Name: {found_pokemon.name.capitalize()}")
            print(f"Type(s): {', '.join(found_pokemon.types)}")
            print(f"Pokedex ID: {found_pokemon.dex}")
            return found_pokemon
    except Exception as e:
        print(f"Pokemon not found.")

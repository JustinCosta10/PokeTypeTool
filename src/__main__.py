from Pokemon import Pokemon
import poke_db
import dex_api
import types

def main():
    # connecting to DB. Passing variable conn into db functions as parameter db_connection
    conn = poke_db.establish_db()
    cursor = conn.cursor()
    user_pokemon_input = input("Enter Pokemon: ")
    try:
        pypokedex_match = dex_api.get_pokemon(user_pokemon_input)
        pokemon = Pokemon(pypokedex_match.dex, pypokedex_match.name.capitalize(), pypokedex_match.types)
        poke_db.insert_pokemon(pokemon, 1, conn)
    except Exception as e:
        print("Adding pokemon failed.")

    cursor.execute("""
        SELECT * from pokemon;
    """)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    poke_db.delete_pokemon(pokemon, conn)

if __name__ == "__main__":
    main()

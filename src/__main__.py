from Pokemon import Pokemon
import poke_db
import dex_api
import poke_types
import tkinter as tk

def test():
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

def on_calculate():
    type_1 = type_1_entry.get()
    type_2 = type_2_entry.get()

        # Call your existing function and update the result label
    try:
        result = poke_types.create_type_list(type_1, type_2)
        result_label.config(text=f"Result: {result}")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

def main():
    root = tk.Tk()
    type1_input = tk.StringVar()
    type2_input = tk.StringVar()
    root.geometry("350x450")

    root.title("Poke Type Planner")
    tk.Label(root, text="Pokemon:").pack()
    pokemon_entry = tk.Entry(root, textvariable=type1_input)
    pokemon_entry.pack(pady=10)
    def on_calculate():
        pokemon_input = pokemon_entry.get()
        try:
            pokemon = dex_api.get_pokemon(pokemon_input)
        except Exception as e:
            result_label.config(text=f"API Error: {str(e)}")

        try:
            print(pokemon.types)
            if len(pokemon.types) == 2:
                type1 = pokemon.types[0]
                type2 = pokemon.types[1]
                result = poke_types.create_type_list(type1, type2)
                result_label.config(text=f"{result}")
            if len(pokemon.types) == 1:
                type1 = pokemon.types[0]
                result = poke_types.create_type_list(type1)
                result_label.config(text=f"{result}")
        except Exception as e:
            result_label.config(text=f"Type List Error: {str(e)}")

    button = tk.Button(root, text="Calculate Type Matchups", command=on_calculate)
    button.pack(pady=10)
    result_label = tk.Label(root)
    result_label.pack(pady=10)
    root.mainloop()
if __name__ == "__main__":
    main()
ß

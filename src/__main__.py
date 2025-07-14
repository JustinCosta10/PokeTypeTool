import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from Pokemon import Pokemon
import poke_db
import dex_api
import poke_types
import json
import os

import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

class PokeTypePlanner:
    def __init__(self, root):
        # Load Pokemon data for autocomplete
        self.load_pokemon_data()
        self.pokemon_types = [
        "Normal", "Fire", "Water", "Electric", "Grass", "Ice",
        "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug",
        "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"
        ]
        self.type_colors = [
        "#A8A77A",  # Normal
        "#EE8130",  # Fire
        "#6390F0",  # Water
        "#F7D02C",  # Electric
        "#7AC74C",  # Grass
        "#96D9D6",  # Ice
        "#C22E28",  # Fighting
        "#A33EA1",  # Poison
        "#E2BF65",  # Ground
        "#A98FF3",  # Flying
        "#F95587",  # Psychic
        "#A6B91A",  # Bug
        "#B6A136",  # Rock
        "#735797",  # Ghost
        "#6F35FC",  # Dragon
        "#705746",  # Dark
        "#B7B7CE",  # Steel
        "#D685AD"   # Fairy
        ]
        self.root = root
        self.root.geometry("350x2000")
        self.root.title("Poke Type Planner")
        
        # Define better font families
        self.fonts = {
            'title': ('Helvetica', 16, 'bold'),
            'entry': ('Arial', 11),
            'button': ('Arial', 10, 'bold'),
            'type_name': ('Arial', 10, 'bold'),
            'type_effect': ('Arial', 9, 'bold'),
            'autocomplete': ('Arial', 10)
        }

        # Input Variables for Text Boxes
        self.pokemon_input = tk.StringVar()
        self.pokemon_input.trace_add('write', self.on_text_change)

        # Widgets ###
        # Pokemon Entry Widget - Text Box
        self.pokemon_entry = tk.Entry(root, textvariable=self.pokemon_input, 
                                     font=self.fonts['entry'], highlightthickness=0)
        self.pokemon_entry.grid(row=1, column=0, columnspan=2, pady=1)
        
        # Autocomplete Listbox (initially hidden)
        self.autocomplete_frame = tk.Frame(root)
        self.autocomplete_listbox = tk.Listbox(self.autocomplete_frame, height=6, width=20,
                                              font=self.fonts['autocomplete'])
        self.autocomplete_listbox.bind('<ButtonRelease-1>', self.on_select_pokemon)
        self.autocomplete_listbox.bind('<Return>', self.on_select_pokemon)
        self.autocomplete_listbox.pack()
        self.autocomplete_visible = False

        # Calculate Type Matchups - Finds all type matchups for the pokemon entered into text box
        self.button = tk.Button(root, text="Go", command=self.on_find_pokemon, 
                               relief="groove", font=self.fonts['button'])
        self.button.grid(row=1, column=0, columnspan=2, pady=(0,5), padx=(135,0))

        # Pokemon Sprite - Reserve space for the sprite
        placeholder_image = Image.new("RGBA", (96, 96), (255, 255, 255, 0))  # Transparent image
        self.placeholder_tk_image = ImageTk.PhotoImage(placeholder_image)
        self.image_label = tk.Label(root, image=self.placeholder_tk_image)
        self.image_label.grid(row=0, column=0, columnspan=2, pady=5)

        # Configure rows and columns
        self.root.grid_rowconfigure(0, weight=0)
        self.root.grid_rowconfigure(1, weight=0)
        self.root.grid_rowconfigure(2, weight=0)
        self.root.grid_rowconfigure(3, weight=0)
        self.root.grid_columnconfigure(0, weight=1)

        # Canvas squares for Pokémon types
        self.canvas_list = []

        self.create_canvas_squares()

    def create_canvas_squares(self):
        square_size = 30  # Size of each square
        starting_row = 3   # Start placing squares below the search section

        for i, type_name in enumerate(self.pokemon_types):
            canvas = tk.Canvas(
                self.root,
                width=square_size * 6,
                height=square_size,
                bg= self.type_colors[i],
                highlightthickness=2,
                highlightbackground="black"
            )
            # Stack vertically
            canvas.grid(row=starting_row + i, column=0, padx=2, pady=2)
            canvas.create_text(
                square_size * 3, square_size // 2,
                text=type_name, font=self.fonts['type_name'], fill="black"
            )
            corner_text = canvas.create_text(
                square_size * 6 - 5, 5,  # Top-right corner
                text="", font=self.fonts['type_effect'], fill="black", anchor="ne"
            )

            self.canvas_list.append((canvas, corner_text))

    def load_pokemon_data(self):
        """Load Pokemon names from the local JSON file for autocomplete"""
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            json_path = os.path.join(script_dir, 'pokemon_data.json')
            with open(json_path, 'r') as f:
                pokemon_data = json.load(f)
            self.pokemon_names = [pokemon['name'].capitalize() for pokemon in pokemon_data]
        except Exception as e:
            print(f"Could not load Pokemon data: {e}")
            self.pokemon_names = []

    def on_text_change(self, *args):
        """Handle text changes in the search box for autocomplete"""
        current_text = self.pokemon_input.get().lower()
        
        if len(current_text) < 2:
            self.hide_autocomplete()
            return
            
        # Filter Pokemon names that start with the current text
        matches = [name for name in self.pokemon_names if name.lower().startswith(current_text)][:10]
        
        if matches:
            self.show_autocomplete(matches)
        else:
            self.hide_autocomplete()

    def show_autocomplete(self, matches):
        """Show the autocomplete dropdown with matching Pokemon"""
        self.autocomplete_listbox.delete(0, tk.END)
        for match in matches:
            self.autocomplete_listbox.insert(tk.END, match)
        
        if not self.autocomplete_visible:
            self.autocomplete_frame.grid(row=2, column=0, columnspan=2, sticky='ew', padx=2)
            self.autocomplete_visible = True

    def hide_autocomplete(self):
        """Hide the autocomplete dropdown"""
        if self.autocomplete_visible:
            self.autocomplete_frame.grid_remove()
            self.autocomplete_visible = False

    def on_select_pokemon(self, event):
        """Handle Pokemon selection from autocomplete"""
        selection = self.autocomplete_listbox.curselection()
        if selection:
            selected_pokemon = self.autocomplete_listbox.get(selection[0])
            self.pokemon_input.set(selected_pokemon)
            self.hide_autocomplete()
            self.on_find_pokemon()

    def on_find_pokemon(self):
        pokemon_input = self.pokemon_input.get()

        try:
            # Simulating the API call
            pokemon = dex_api.get_pokemon(pokemon_input)
        except Exception as e:
            self.result_label.config(text=f"API Error: {str(e)}")
            return

        try:
            # Fetch and display the image
            response = requests.get(pokemon.sprites.front.get('default'))
            response.raise_for_status()

            img_data = BytesIO(response.content)
            pil_image = Image.open(img_data)
            tk_image = ImageTk.PhotoImage(pil_image)

            # Update the pre-existing image_label
            self.image_label.config(image=tk_image, bg=None)
            self.image_label.image = tk_image
        except Exception as e:
            self.result_label.config(text=f"Image Error: {str(e)}")
            return

        try:
            # Simulating poke_types.create_type_list call
            if len(pokemon.types) == 2:
                result = poke_types.create_type_list(pokemon.types[0], pokemon.types[1])
            else:
                result = poke_types.create_type_list(pokemon.types[0])

            self.pokemon_type_matchups = result
            for i, (canvas, corner_text) in enumerate(self.canvas_list):
                if self.pokemon_type_matchups[i] == "1x":
                    canvas.itemconfig(corner_text, text="")
                else:
                    canvas.itemconfig(corner_text, text=self.pokemon_type_matchups[i])
        except Exception as e:
            self.result_label.config(text=f"Type List Error: {str(e)}")
            return


#def test():
#        # connecting to DB. Passing variable conn into db functions as parameter db_connection
#    conn = poke_db.establish_db()
#    cursor = conn.cursor()
#    user_pokemon_input = input("Enter Pokemon: ")
#    try:
#        pypokedex_match = dex_api.get_pokemon(user_pokemon_input)
#        pokemon = Pokemon(pypokedex_match.dex, pypokedex_match.name.capitalize(), pypokedex_match.types)
#        poke_db.insert_pokemon(pokemon, 1, conn)
#    except Exception as e:
#        print("Adding pokemon failed.")
#
#    cursor.execute("""
#        SELECT * from pokemon;
#    """)
#    rows = cursor.fetchall()
#    for row in rows:
#        print(row)
#    poke_db.delete_pokemon(pokemon, conn)
#

def main():
    root = tk.Tk()
    app = PokeTypePlanner(root)
    root.mainloop()

if __name__ == "__main__":
    main()

import sqlite3
import os
from Pokemon import Pokemon

#Not used at all in the current version, but may be used as features are added

#Creates database, tables and inserts a test team
def establish_db():
    conn = sqlite3.connect("../db/poke_db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pokemon_team(
        team_id INTEGER PRIMARY KEY AUTOINCREMENT,
        team_name TEXT NOT NULL
    );
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pokemon(
        dex_id INTEGER PRIMARY KEY,
        pokemon_name TEXT NOT NULL UNIQUE,
        team_id INTEGER NOT NULL,
        FOREIGN KEY (team_id) REFERENCES pokemon_team(team_id)
    );
    """)
    cursor.execute("""
    CREATE TRIGGER IF NOT EXISTS limit_team_entries
    BEFORE INSERT ON pokemon
    WHEN (SELECT COUNT(*) FROM pokemon WHERE team_id = NEW.team_id) >= 6
    BEGIN
    SELECT RAISE(FAIL, 'Team cannot have more than 6 Pokémon.');
    END;
""")
    cursor.execute("""
    INSERT OR IGNORE INTO pokemon_team (team_id, team_name)
    VALUES (1, "Default Team")
    """)
    return conn

# Parameters:
# pokemon - takes an instance of the dataclass Pokemon
# team_id - the team id that the Pokemon is supposed to be associated with
# db_connection - The current database connection passed in to avoid redundant connections
def insert_pokemon(pokemon: Pokemon, team_id, db_connection):
    try:
        conn = db_connection
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO pokemon (dex_id, pokemon_name, team_id)
        VALUES (:dex_id, :pokemon_name, :team_id)
        """, {
            "dex_id": pokemon.dex_id,
            "pokemon_name": pokemon.name,
            "team_id": team_id
        })
        conn.commit()
        print(f"Successfully added Pokémon '{pokemon.name}' to team ID {team_id}.")
    except sqlite3.IntegrityError as e:
        print(f"{e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Parameters:
# pokemon - takes an instance of the dataclass Pokemon
# db_connection - The current database connection passed in to avoid redundant connections
def delete_pokemon(pokemon: Pokemon, db_connection):
    try:
        conn = db_connection
        cursor = conn.cursor()

        cursor.execute("DELETE FROM pokemon WHERE pokemon_name = ?", (pokemon.name,))

        if cursor.rowcount > 0:
            conn.commit()
            print(f"Pokémon '{pokemon.name}' deleted successfully.")
            return True
        else:
            print(f"Pokémon '{pokemon.name}' not found.")
            return False
    except sqlite3.DatabaseError as e:
        print(f"Database error: {e}")
        return False

pokemon_types = ["normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy"]

# Rows represent attacking types, Columns represent defending types
# 0 = standard, 1 = ineffective, 2 = super effective, 3 = immune
attacking_types = (
    #0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 0, 0, 1, 0], #Normal Row     0
    [0, 1, 1, 0, 2, 2, 0, 0, 0, 0, 0, 2, 1, 0, 1, 0, 2, 0], #Fire Row       1
    [0, 2, 1, 0, 1, 0, 0, 0, 2, 0, 0, 0, 2, 0, 1, 0, 0, 0], #Water Row      2
    [0, 0, 2, 1, 1, 0, 0, 0, 3, 2, 0, 0, 0, 0, 1, 0, 0, 0], #Electric Row   3
    [0, 1, 2, 0, 1, 0, 0, 1, 2, 1, 0, 1, 2, 0, 1, 0, 1, 0], #Grass Row      4
    [0, 1, 1, 0, 2, 1, 0, 0, 2, 2, 0, 0, 0, 0, 2, 0, 1, 0], #Ice Row        5
    [2, 0, 0, 0, 0, 2, 0, 1, 0, 1, 1, 1, 2, 3, 0, 2, 2, 1], #Fighting Row   6
    [0, 0, 0, 0, 2, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 3, 2], #Poison Row     7
    [0, 2, 0, 2, 1, 0, 0, 2, 0, 3, 0, 1, 2, 0, 0, 0, 2, 0], #Ground Row     8
    [0, 0, 0, 1, 2, 0, 2, 0, 0, 0, 0, 2, 1, 0, 0, 0, 1, 0], #Flying Row     9
    [0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 1, 0, 0, 0, 0, 3, 1, 0], #Psychic Row    10
    [0, 1, 0, 0, 2, 0, 1, 1, 0, 1, 2, 0, 0, 1, 0, 2, 1, 1], #Bug Row        11
    [0, 2, 0, 0, 0, 2, 1, 0, 1, 2, 0, 2, 0, 0, 0, 0, 1, 0], #Rock Row       12
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 1, 0, 0], #Ghost Row      13
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 3], #Dragon Row     14
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 2, 0, 1, 0, 1], #Dark Row       15
    [0, 1, 1, 1, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 2], #Steel Row      16
    [0, 1, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 2, 2, 1, 0]  #Fairy Row      17
    )
# Transposed to more quickly access defending type matchup without unneccessary looping
defending_types = (
    [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0],
    [0, 1, 2, 0, 1, 1, 0, 0, 2, 0, 0, 1, 2, 0, 0, 0, 1, 1],
    [0, 1, 1, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 2, 1, 1, 1, 2, 0, 2, 1, 2, 0, 2, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1, 1, 0, 0, 1, 0, 2],
    [0, 0, 0, 0, 1, 0, 1, 1, 2, 0, 2, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 2, 3, 2, 2, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 1, 2, 1, 0, 3, 0, 0, 1, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 2, 0, 2, 0, 2, 0, 0],
    [0, 2, 0, 0, 1, 0, 1, 0, 1, 2, 0, 0, 2, 0, 0, 0, 0, 0],
    [1, 1, 2, 0, 2, 0, 2, 1, 2, 1, 0, 0, 0, 0, 0, 0, 2, 0],
    [3, 0, 0, 0, 0, 0, 3, 1, 0, 0, 0, 1, 0, 2, 0, 2, 0, 0],
    [0, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 3, 2, 0, 1, 0, 1, 0, 2],
    [1, 2, 0, 0, 1, 1, 2, 3, 2, 1, 1, 1, 1, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 1, 0, 0, 3, 1, 2, 0]
    )

type_key = {
    0: "Standard",
    1: "Not very effective",
    2: "Super effective",
    3: "No damage"
}

def type_input_lowercase():
    type_input = input("Enter type: ")
    type_choice = type_input.lower()
    return type_choice

# need to either rewrite or heavily customize to combine the two types defensively
def find_type_matchups(type1, type2 = None):
    try:
        type1_index = pokemon_types.index(type1)
        display_type_1 = type1.capitalize()

        print(f"{display_type_1} Defense:\n")
        for col_index, type_value in enumerate(defending_types[type1_index]):
            type_relationship = type_key.get(type_value, "No relationship found")
            if(type_value != 0):
                print(f"{pokemon_types[col_index].capitalize()}: {type_relationship}")
        print("\n")
    except Exception as e:
        print(f"Invalid type. Error: {e}")
    if type2 is not None:
        try:
            type2_index = pokemon_types.index(type2)
            display_type_2 = type2.capitalize()
            print(f"{display_type_2} Defense:\n")
            for col_index, type_value in enumerate(defending_types[type2_index]):
                type_relationship = type_key.get(type_value, "No relationship found")
                if(type_value != 0):
                    print(f"{pokemon_types[col_index].capitalize()}: {type_relationship}")
            print("\n")
        except Exception as e:
            print(f"Invalid type. Error: {e}")

type_choice_1 = type_input_lowercase()
type_choice_2 = type_input_lowercase()
find_type_matchups(type_choice_1, type_choice_2)
find_type_matchups("water")
find_type_matchups("water", "poison")
find_type_matchups("water", "bongo")

# Need to switch type numbers out. 0 should be standard, -1 should be not very effective, 1 should be super effective, and immune should be null or None
# Then we can mathematically solve the type combinations strengths and weaknesses with these conditions:
# if type1 + type2 = 0 it is standard effectiveness
# if type1 + type2 = 2 it is 4x effective
# if type1 + type2 = null or TypeError the pokemon is immune, because one immune typing immunizes the type combination.

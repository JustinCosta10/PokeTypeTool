pokemon_types = ["normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy"]
# For reference checking while building program. Negatives and None make chart unreadably messy.
# 0 = standard, 1 = ineffective, 2 = super effective, 3 = immune
#attacking_types = (
#    #0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17
#    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 0, 0, 1, 0], #Normal Row     0
#    [0, 1, 1, 0, 2, 2, 0, 0, 0, 0, 0, 2, 1, 0, 1, 0, 2, 0], #Fire Row       1
#    [0, 2, 1, 0, 1, 0, 0, 0, 2, 0, 0, 0, 2, 0, 1, 0, 0, 0], #Water Row      2
#    [0, 0, 2, 1, 1, 0, 0, 0, 3, 2, 0, 0, 0, 0, 1, 0, 0, 0], #Electric Row   3
#    [0, 1, 2, 0, 1, 0, 0, 1, 2, 1, 0, 1, 2, 0, 1, 0, 1, 0], #Grass Row      4
#    [0, 1, 1, 0, 2, 1, 0, 0, 2, 2, 0, 0, 0, 0, 2, 0, 1, 0], #Ice Row        5
#    [2, 0, 0, 0, 0, 2, 0, 1, 0, 1, 1, 1, 2, 3, 0, 2, 2, 1], #Fighting Row   6
#    [0, 0, 0, 0, 2, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 3, 2], #Poison Row     7
#    [0, 2, 0, 2, 1, 0, 0, 2, 0, 3, 0, 1, 2, 0, 0, 0, 2, 0], #Ground Row     8
#    [0, 0, 0, 1, 2, 0, 2, 0, 0, 0, 0, 2, 1, 0, 0, 0, 1, 0], #Flying Row     9
#    [0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 1, 0, 0, 0, 0, 3, 1, 0], #Psychic Row    10
#    [0, 1, 0, 0, 2, 0, 1, 1, 0, 1, 2, 0, 0, 1, 0, 2, 1, 1], #Bug Row        11
#    [0, 2, 0, 0, 0, 2, 1, 0, 1, 2, 0, 2, 0, 0, 0, 0, 1, 0], #Rock Row       12
#    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 1, 0, 0], #Ghost Row      13
#    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 3], #Dragon Row     14
#    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 2, 0, 1, 0, 1], #Dark Row       15
#    [0, 1, 1, 1, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 2], #Steel Row      16
#    [0, 1, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 2, 2, 1, 0]  #Fairy Row      17
#    )
# Transposed to more quickly access defensive type matchups without unneccessary looping
# Used actual intended values for the chart to work well for type math
# Chose these numbers so that the dual type matchups could be mathematically determined
# if type1 + type2 = 0 it is standard effectiveness
# if type1 + type2 = 2 it is 4x effective
# if type1 + type2 = null or TypeError the pokemon is immune, because one immune typing immunizes the type combination.
types = (
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0],
    [0, -1, 1, 0, -1, -1, 0, 0, 1, 0, 0, -1, 1, 0, 0, 0, -1, -1],
    [0, -1, -1, 1, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0],
    [0, 0, 0, -1, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, -1, 0],
    [0, 1, -1, -1, -1, 1, 0, 1, -1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, -1, -1, 0, 0, -1, 0, 1],
    [0, 0, 0, 0, -1, 0, -1, -1, 1, 0, 1, -1, 0, 0, 0, 0, 0, -1],
    [0, 0, 1, None, 1, 1, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, -1, 1, -1, 0, None, 0, 0, -1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 1, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, -1, 0, -1, 0, -1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [-1, -1, 1, 0, 1, 0, 1, -1, 1, -1, 0, 0, 0, 0, 0, 0, 1, 0],
    [None, 0, 0, 0, 0, 0, None, -1, 0, 0, 0, -1, 0, 1, 0, 1, 0, 0],
    [0, -1, -1, -1, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, None, 1, 0, -1, 0, -1, 0, 1],
    [-1, 1, 0, 0, -1, -1, 1, None, 1, -1, -1, -1, -1, 0, -1, 0, -1, -1],
    [0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 0, None, -1, 1, 0]
    )

type_key = {
    -2: "1/4x",
    -1: "1/2x",
    0: "1x",
    1: "2x",
    2: "4x",
    None: "Immune"
}

def type_input_lowercase():
    type_input = input("Enter type: ")
    type_choice = type_input.lower()
    return type_choice

def find_type_values(type1_input, type2_input = None):
    type1 = type1_input.lower()
    type1_index = pokemon_types.index(type1)
    type1_array = types[type1_index]

    if type2_input is None:
        print(type1_array)
        return type1_array

    type2 = type2_input.lower()
    type2_index = pokemon_types.index(type2)
    type2_array = types[type2_index]
    combined_type_array = []
    for i in range (len(type1_array)):
        if type1_array[i] is None or type2_array[i] is None:
            combined_type_array.append(None)
        else:
            combined_type_array.append(type1_array[i] + type2_array[i])
    print (combined_type_array)
    return combined_type_array

def find_type_matchups(type_values: list) -> str:
    try:
        output = []
        for i, type_value in enumerate(type_values):
            type_name = pokemon_types[i]
            type_relationship = type_key.get(type_value, "No relationship found")
            output.append(f"{type_relationship}")
        return output
    except Exception as e:
        return f"Error: {e}"

def find_type_matchups_print(type_values : list):
    try:
        print(f"Defense:\n")
        for i, type_value in enumerate(type_values):
            type_name = pokemon_types[i]
            type_relationship = type_key.get(type_value, "No relationship found")
            print(f"{type_name}: {type_relationship}")
        print("\n")
    except Exception as e:
        print(f"Error: {e}")

def create_type_list(type1, type2 = None):
    if type2 is None:
        type_values = find_type_values(type1)
        type_output = find_type_matchups(type_values)
    else:
        type_values = find_type_values(type1, type2)
    type_output = find_type_matchups(type_values)
    return type_output



#Example Implementation
#type_choice_1 = type_input_lowercase()
#type_choice_2 = type_input_lowercase()
#pokemon_type_values = find_type_values(type_choice_1, type_choice_2)
#pokemon_type_matchups = find_type_matchups(pokemon_type_values)
#print(pokemon_type_matchups)

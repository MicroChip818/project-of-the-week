import random
import sys

def scramble_cube(moves_per_scramble, num_scrambles, moves_per_line): # If you want to copy the code, copy lines 1 and 4-23, then call the function with your own parameters
    faces = ["F", "B", "U", "D", "L", "R"] # All 6 possible faces
    modifiers = ["", "'", "2"] # 2 possible modifiers
    for i in range(num_scrambles): # Repeat this for every scramble
        scramble = ""
        prev = ""
        face = ""
        newline = ""
        for i in range(moves_per_scramble): # Repeat this for every move per scramble
            if (i + 1) % moves_per_line == 0: # New line after a certain number of movesww
                newline = "\n"
            else:
                newline = ""
            while face == prev: # Ensures the next move uses a different face
                face = faces[random.randint(0, 5)]
            mod = modifiers[random.randint(0, 2)]
            scramble += f"{face}{mod} {newline}"
            prev = face
        print(scramble)
        print() # New line to separate scrambles

if __name__ == "__main__": # The following code is only necessary in a GitHub Workflows Project combined with a YAML file
    DEFAULT_MOVES_PER_SCRAMBLE = 20
    DEFAULT_NUM_SCRAMBLES = 3
    DEFAULT_MOVES_PER_LINE = 5

    def get_int(arg_index, default, name): # Custom argument inputs
        try:
            return int(sys.argv[arg_index])
        except IndexError:
            return default
        except ValueError:
            print(f"Invalid value for {name}. Must be an integer.")
            sys.exit(1)

    moves_per_scramble = get_int(1, DEFAULT_MOVES_PER_SCRAMBLE, "moves per scramble")
    num_scrambles = get_int(2, DEFAULT_NUM_SCRAMBLES, "number of scrambles")
    moves_per_line = get_int(3, DEFAULT_MOVES_PER_LINE, "moves per line")

    scramble_cube(moves_per_scramble, num_scrambles, moves_per_line) # Call the function with required arguments

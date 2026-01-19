import random
import sys

def scramble_cube(moves_per_scramble, num_scrambles, moves_per_line):
    faces = ["F", "B", "U", "D", "L", "R"]
    modifiers = ["", "'", "2"]
    for i in range(num_scrambles):
        scramble = ""
        prev = ""
        face = ""
        newline = ""
        for i in range(moves_per_scramble):
            if (i + 1) % moves_per_line == 0:
                newline = "\n"
            else:
                newline = ""
            while face == prev:
                face = faces[random.randint(0, 5)]
            mod = modifiers[random.randint(0, 2)]
            scramble += f"{face}{mod} {newline}"
            prev = face
        print(scramble)
        print()

if __name__ == "__main__":
    DEFAULT_MOVES_PER_SCRAMBLE = 20
    DEFAULT_NUM_SCRAMBLES = 3
    DEFAULT_MOVES_PER_LINE = 5

    def get_int(arg_index, default, name):
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

    scramble_cube(moves_per_scramble, moves_per_line, num_scrambles)

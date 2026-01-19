import random
import sys

def scramble_cube(moves_per_scramble, moves_per_line, num_scrambles):
    faces = ["F", "B", "U", "D", "L", "R"]
    modifiers = ["", "'", "2"]
    for i in range(num_scrambles):
        scramble = ""
        prev = ""
        face = ""
        newline = ""
        for i in range(moves):
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
    moves_per_scramble = int(sys.argv[1])
    num_scrambles   = int(sys.argv[2])
    moves_per_line  = int(sys.argv[3])

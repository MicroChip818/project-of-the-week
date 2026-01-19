import random
def scramble_cube(moves, moves_per_line):
    faces = ["F", "B", "U", "D", "L", "R"]
    modifiers = ["", "'", "2"]
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

if __name__ == "__main__":
    scramble_cube(20, 5)

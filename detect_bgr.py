from re import I
from vpython import *
from  cube_by_color import rubiks_cube_solver_color
from change_X import *
from conditional import move_table
from solution import solution_of_scramble
import time 
import keyboard
# Store each cubelet with its stickers
COOLDOWN = 0.5
def tokenize_moves(s: str) -> list[str]:
        return s.strip().split()

def rubiks_cube_solver(scramble,solution):
    # Cubelet positions
    cubes = []  # each item is {'body': ..., 'stickers': [...]}
    scene = canvas(
        userzoom = False,
        userspin = False,
        range = 100,
        forward = vector(-0.2, -0.5, -0.5)
    )
    distant_light(direction=vector( 1, 1, 1), color=color.white)
    # Sticker size and offset
    sticker_size = 17
    sticker_thickness = 0.1
    offset = 9.5

    # Define sticker face directions
    face_vectors = {
        'U': vector(0, 1, 0),
        'D': vector(0, -1, 0),
        'F': vector(0, 0, 1),
        'B': vector(0, 0, -1),
        'L': vector(-1, 0, 0),
        'R': vector(1, 0, 0)
    }

    # Color mapping
    face_colors = {
        'U': color.white,
        'D': color.yellow,
        'F': color.green,
        'B': color.blue,
        'L': color.orange,
        'R': color.red
    }
    i =0

    # Create cubelets
    for x in [-20, 0, 20]:
        for y in [20, 0, -20]:
            for z in [-20, 0, 20]:
                cubelet = {}
                center = vector(x, y, z)
                # Invisible cube body
                cubelet['body'] = box(pos=center, size=vector(19,19,19), color = color.gray(0.8))

                # Add stickers
                stickers = []
                for face, normal in face_vectors.items():
                    
                    # Only add stickers on visible faces
                    if (face == 'U' and y == 20) or (face == 'D' and y == -20) or \
                    (face == 'F' and z == 20) or (face == 'B' and z == -20) or \
                    (face == 'L' and x == -20) or (face == 'R' and x == 20):
                        s = box(pos= center + normal * offset,size=vector(sticker_thickness, sticker_size, sticker_size),color=face_colors[face], axis = normal  )
                        stickers.append(s)
                cubelet['stickers'] = stickers
                cubes.append(cubelet)


    # Init rotation state
    rotating = [False] * 54
    input_map = {
        'U': 0,   'U\'': 1,  'U2': 2,
        'L': 3,   'L\'': 4,  'L2': 5,
        'F': 6,   'F\'': 7,  'F2': 8,
        'R': 9,   'R\'': 10, 'R2': 11,
        'B': 12,  'B\'': 13, 'B2': 14,
        'D': 15,  'D\'': 16, 'D2': 17,
        'M': 18,  'M\'': 19, 'M2': 20,
        'E': 21,  'E\'': 22, 'E2': 23,
        'S': 27,  'S\'': 28, 'S2': 29,
        'x': 30,  'x\'': 31, 'x2': 32,
        'y': 33,  'y\'': 34, 'y2': 35,
    }

    def rebuild_notas():
        def extract(i): return [cubes[i]['body']] + cubes[i]['stickers']

        notas = {
            'U': sum([extract(i) for i in (0,1,2, 9,10,11, 18,19,20)], []),
            'L': sum([extract(i) for i in (0,1,2, 3,4,5, 6,7,8)], []),
            'F': sum([extract(i) for i in (2,5,8, 11,14,17, 20,23,26)], []),
            'R': sum([extract(i) for i in (20,19,18, 23,22,21, 26,25,24)], []),
            'B': sum([extract(i) for i in (18,21,24, 9,12,15, 0,3,6)], []),
            'D': sum([extract(i) for i in (8,7,6, 17,16,15, 26,25,24)], []),
            'M': sum([extract(i) for i in (9,10,11,12,13,14,15,16,17)], []),
            'E': sum([extract(i) for i in (3,4,5,12,13,14,21,22,23)], []),
            'S': sum([extract(i) for i in (1,10,19,4,13,22,7,16,25)], []),
            'x': sum([extract(i) for i in range(0,27)], []),
            'y': sum([extract(i) for i in range(0,27)], []),
            'z': sum([extract(i) for i in range(0,27)], []),
        }
        notas.update({
            'u': notas['U'] + notas['E'],
            'l': notas['L'] + notas['M'],
            'f': notas['F'] + notas['S'],
            'r': notas['R'] + notas['M'],
            'b': notas['B'] + notas['S'],
            'd': notas['D'] + notas['E']
        })
        return notas

    # Main loop

    for i in scramble: 
            idx = input_map[i]
            if idx is not None and not rotating[idx]:
                rotating[idx] = True
            rate(60)
            for i, flag in enumerate(rotating):
                if not flag:
                    continue
                face_key, rot_fn, change_fn, notation, axis, origin = move_table[i]
                notas = rebuild_notas()
                rot_fn(notas[face_key], axis=axis, origin=origin, duration=0.1)
                change_fn(cubes)  
                rotating[i] = False
                # print(notation, end=" ", flush=True)
                time.sleep(0.3)
    sol = tokenize_moves(solution)
    for move in sol:
        # Wait for spacebar press (tap)
        # print(f"Press space to perform move: {move}")
        while True:
            if keyboard.is_pressed("space"):
                while keyboard.is_pressed("space"):
                    pass  # Wait for spacebar release
                break

        idx = input_map[move]
        if idx is not None:
            rotating[idx] = True

        rate(60)

        # Process only the current move
        if rotating[idx]:
            face_key, rot_fn, change_fn, notation, axis, origin = move_table[idx]
            notas = rebuild_notas()
            rot_fn(notas[face_key], axis=axis, origin=origin, duration=0.1)
            change_fn(cubes)
            rotating[idx] = False
            # print(notation, end=" ", flush=True)
        time.sleep(0.05)  # small delay to avoid flicker or accidental double-press
    
    # print()  # newline after moves are finishe
    while True:pass

# s_in = input("Type the Scramble:")
# s_in = "R2 F U B2 D F2 L2 D2 U' R2 B2 U R2 F L F D B R' U"
# scramble = tokenize_moves(s_in)

# sol = solution_of_scramble(s_in)
# print('solution:',sol)
# rubiks_cube_solver(scramble,sol)



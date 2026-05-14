from re import I
from vpython import *
from change_X import *
from conditional import move_table
# Store each cubelet with its stickers
def rubiks_cube_simulator():
    # Cubelet positions
    cubes = []  # each item is {'body': ..., 'stickers': [...]}
    scene = canvas(
        title = 'Rubiks Cube Simulator',
        userzoom = False,
        userspin = False,
        range = 100,
        forward = vector(0, -0.5, -0.5)
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


    # initial state of true false 
    rotating = [False] * 54

    # Input mapping FOR
    input_map = {
    'j': 0,  'f': 1,  # u face 
    'd': 3,  'e': 4,  # l face
    'h': 6,  'g': 7,  # f face
    'k': 9,  'i': 10, # r face
    'w': 12, 'o': 13, # b face
    's': 15, 'l': 16, # d face
    '.': 18, 'x': 19, # m face
    '2': 21, '9': 22, # e face
    'n': 27, 'y': 28, # x rotation 
    ';': 30, 'a': 31, # y rotation
    'p': 33, 'q': 34, # z rotation
    # ',': 36, 'c': 37, #wide u move 
    # 'v': 39, 'r': 40, #wide l move
    # '0': 42, '1': 43, #wide f move
    # 'u': 45, 'i': 46, #wide r move
    # 'z': 51, 'o': 52, #wide d move
    }

    def key_input(evt):
        if not hasattr(evt, 'key'):
            return
        k = evt.key.lower()
        if any(rotating):
            return
        idx = input_map.get(k)
        if idx is not None and not rotating[idx]:
            rotating[idx] = True
        
    scene.bind('keydown', key_input)

    # Map face notations to cubelets
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
    while True:
        rate(60)
        for i, flag in enumerate(rotating):
            if not flag:
                continue
            face_key, rot_fn, change_fn, notation, axis, origin = move_table[i]
            notas = rebuild_notas()
            rot_fn(notas[face_key], axis=axis, origin=origin, duration=0.1)
            change_fn(cubes)  
            rotating[i] = False
            print(notation, end=" ", flush=True)
        
          
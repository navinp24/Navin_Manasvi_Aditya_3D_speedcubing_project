def change_for_kociemba(raw):
    chunks = [raw[i*9:(i+1)*9] for i in range(6)] # 9x^6 array 
    up_raw, left_raw, front_raw, right_raw, back_raw, down_raw = chunks
    # replacement 
    colour_to_face = {'W':'U', 'R':'R', 'G':'F', 'Y':'D', 'O':'L', 'B':'B'}
    def map_face(raw: str) -> str:
        return ''.join(colour_to_face[c] for c in raw)

    up    = map_face(up_raw)
    left  = map_face(left_raw)
    front = map_face(front_raw)
    right = map_face(right_raw)
    back  = map_face(back_raw)
    down  = map_face(down_raw)

    cubestring = up + right + front + down + left + back
    return cubestring

raw = 'WWWWWWWWWOOOOOOOOOGGGGGGGGGRRRRRRRRRBBBBBBBBBYYYYYYYYY'
changed = change_for_kociemba(raw)
def change_u(c): 
    cpy = c.copy()
    c[0],  c[1],  c[2],  c[9],  c[11],  c[18],  c[19],  c[20] = (
        cpy[2], cpy[11], cpy[20],
        cpy[1], cpy[19],
        cpy[0], cpy[9],  cpy[18]
    )
def change_up(c):
    for _ in range(3): 
        change_u(c)

def change_u2(c):
    for _ in range(2): 
        change_u(c)
# bottom layer
def change_d(c):
    cpy = c.copy()
    c[8],  c[7],  c[6],  c[17], c[15], c[26], c[25], c[24] = (
        cpy[6], cpy[15], cpy[24],
        cpy[7], cpy[25],
        cpy[8], cpy[17], cpy[26]
    )
def change_dp(c):
    for _ in range(3):
        change_d(c)
def change_d2(c):
    for _ in range(2): 
        change_d(c)

# front layer 
def change_f(c):
    cpy = c.copy()
    c[2],  c[5],  c[8],  c[11], c[17], c[20], c[23], c[26] = (
        cpy[8], cpy[17], cpy[26],
        cpy[5], cpy[23],
        cpy[2], cpy[11], cpy[20]
    )
def change_fp(c):
   for _ in range(3):
        change_f(c)
def change_f2(c):
    for _ in range(2): 
        change_f(c)
# back layer
def change_b(c):
    cpy = c.copy()
    c[18], c[21], c[24], c[9],  c[15], c[0],  c[3],  c[6] = (
        cpy[24], cpy[15], cpy[6],
        cpy[21], cpy[3],
        cpy[18], cpy[9],  cpy[0]
    )
def change_bp(c):
    for _ in range(3):
        change_b(c)
def change_b2(c):
    for _ in range(2): 
        change_b(c)
# left layer
def change_l(c):
    cpy = c.copy()
    c[0],  c[3],  c[6],  c[1],  c[7],  c[2],  c[5],  c[8] = (
        cpy[6], cpy[7], cpy[8],
        cpy[3], cpy[5], 
        cpy[0],cpy[1], cpy[2]
    )
def change_lp(c):
    for _ in range(3):
        change_l(c)
def change_l2(c):
    for _ in range(2):
        change_l(c)
# right layer
def change_r(c):
    cpy = c.copy()
    c[20], c[23], c[26], c[19], c[25], c[18], c[21], c[24] = (
        cpy[26], cpy[25], cpy[24],
        cpy[23], cpy[21], cpy[20],
        cpy[19], cpy[18]
    )
def change_rp(c):
    for _ in range(3):
        change_r(c)
def change_r2(c):
    for _ in range(2):
        change_r(c)
# middle layer 
def change_m(c):
    cpy = c.copy()
    c[9],  c[10],  c[11],  c[12], c[14], c[15], c[16], c[17] = (
        cpy[15], cpy[12], cpy[9],
        cpy[16], cpy[10],
        cpy[17],cpy[14], cpy[11]
    )
def change_mp(c):
    for _ in range(3):
        change_m(c)
 
# S layer motion 
def change_s(c):
    cpy = c.copy()
    c[1],  c[10],  c[19],  c[4], c[22], c[7], c[16], c[25] = (
        cpy[19], cpy[22], cpy[25],
        cpy[10], cpy[16],
        cpy[1], cpy[4], cpy[7]
    )
def change_sp(c):
    for _ in range(3):
        change_s(c)
# E layer motion
def change_e(c):
    cpy = c.copy()
    c[3],  c[4],  c[5],  c[12], c[14], c[21], c[22], c[23] = (
        cpy[21], cpy[12], cpy[3],
        cpy[22], cpy[4],
        cpy[23], cpy[14], cpy[5]
    )
def change_ep(c):
    for _ in range(3):
        change_e(c)
# for x rotation
def change_x(c):
    cpy = c.copy()
    c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8],c[9],c[10],c[11],c[12],c[13],c[14],c[15],c[16],c[17],c[18],c[19],c[20],c[21],c[22],c[23],c[24],c[25],c[26] =(
        cpy[6],cpy[3],cpy[0],
        cpy[7],cpy[4],cpy[1],
        cpy[8],cpy[5],cpy[2],
        cpy[15],cpy[12],cpy[9],
        cpy[16],cpy[13],cpy[10],
        cpy[17],cpy[14],cpy[11],
        cpy[24],cpy[21],cpy[18],
        cpy[25],cpy[22],cpy[19],
        cpy[26],cpy[23],cpy[20]
    )   
def change_xp(c):
    for _ in range(3):
        change_x(c)
def change_x2(c):
    for _ in range(2):
        change_x(c)
# for y rotation
def change_y(c):
    cpy = c.copy()
    c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8],c[9],c[10],c[11],c[12],c[13],c[14],c[15],c[16],c[17],c[18],c[19],c[20],c[21],c[22],c[23],c[24],c[25],c[26] =(
        cpy[2],cpy[11],cpy[20],
        cpy[5],cpy[14],cpy[23],
        cpy[8],cpy[17],cpy[26],
        cpy[1],cpy[10],cpy[19],
        cpy[4],cpy[13],cpy[22],
        cpy[7],cpy[16],cpy[25],
        cpy[0],cpy[9], cpy[18],
        cpy[3],cpy[12],cpy[21],
        cpy[6],cpy[15],cpy[24]
    )
def change_yp(c):
    for _ in range(3):
        change_y(c)
def change_y2(c):
    for _ in range(2):
        change_y(c)
# for z rotation
def change_z(c):
    cpy = c.copy()
    c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8],c[9],c[10],c[11],c[12],c[13],c[14],c[15],c[16],c[17],c[18],c[19],c[20],c[21],c[22],c[23],c[24],c[25],c[26] =(
        cpy[6],cpy[7],cpy[8],
        cpy[15],cpy[16],cpy[17],
        cpy[24],cpy[25],cpy[26],
        cpy[3],cpy[4],cpy[5],
        cpy[12],cpy[13],cpy[14],
        cpy[21],cpy[22],cpy[23],
        cpy[0],cpy[1],cpy[2],
        cpy[9],cpy[10],cpy[11],
        cpy[18],cpy[19],cpy[20]
    )
def change_zp(c):
    for _ in range(3):
        change_z(c)
def change_z2(c):
    for _ in range(2):
        change_z(c)

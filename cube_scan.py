from  change_X import * 
from vpython import *
import time
import math 
 
def rotate_face(cubies, axis, origin, angle_rad, duration=0.5):
    remaining = angle_rad
    t_end     = time.time() + duration

    while abs(remaining) > 1e-4:
        rate(60)

        now = time.time()
        if now >= t_end:
            dtheta = remaining
        else:
            elapsed = duration - (t_end - now)
            frac    = elapsed / duration
            dtheta  = angle_rad * frac - (angle_rad - remaining)

        for c in cubies:
            c.rotate(angle=-dtheta, axis=axis, origin=origin)

        remaining -= dtheta
        duration   = max(t_end - now, 0.0)

def rotate_face_clk(cubies, axis, origin, duration=0.5):
    rotate_face(cubies, axis, origin,  math.pi/2, duration)

def rotate_face_aclk(cubies, axis, origin, duration=0.5):
    rotate_face(cubies, axis, origin, -math.pi/2, duration)

def rotate_face_double(cubies, axis, origin, duration=0.5):
    rotate_face(cubies, axis, origin,  math.pi,   duration)
move_table =[None]*35
move_table = [
    # U, U', U2 , 012
    ('U', rotate_face_clk,  change_u,  "U",  vector(0,1,0),  vector(0,20,0)),
    ('U', rotate_face_aclk, change_up, "U'", vector(0,1,0),  vector(0,20,0)),
    ('U', rotate_face_double, change_u2, "U2", vector(0,1,0),  vector(0,20,0)),
    # L, L', L2 345
    ('L', rotate_face_clk,  change_l,  "L",  vector(-1,0,0), vector(-20,0,0)),
    ('L', rotate_face_aclk, change_lp, "L'", vector(-1,0,0), vector(-20,0,0)),
    ('L', rotate_face_double, change_l2, "L2", vector(-1,0,0), vector(-20,0,0)),
    # F, F', F2 678
    ('F', rotate_face_clk,  change_f,  "F",  vector(0,0,1),  vector(0,0,20)),
    ('F', rotate_face_aclk, change_fp, "F'", vector(0,0,1),  vector(0,0,20)),
    ('F', rotate_face_double, change_f2, "F2", vector(0,0,1),  vector(0,0,20)),
    # R, R', R2 91011
    ('R', rotate_face_clk,  change_r,  "R",  vector(1,0,0),  vector(20,0,0)),
    ('R', rotate_face_aclk, change_rp, "R'", vector(1,0,0),  vector(20,0,0)),
    ('R', rotate_face_double, change_r2, "R2", vector(1,0,0),  vector(20,0,0)),
    # B, B', B2 121314
    ('B', rotate_face_clk,  change_b,  "B",  vector(0,0,-1), vector(0,0,-20)),
    ('B', rotate_face_aclk, change_bp, "B'", vector(0,0,-1), vector(0,0,-20)),
    ('B', rotate_face_double, change_b2, "B2", vector(0,0,-1), vector(0,0,-20)),
    # D, D', D2 151617
    ('D', rotate_face_clk,  change_d,  "D",  vector(0,-1,0), vector(0,-20,0)),
    ('D', rotate_face_aclk, change_dp, "D'", vector(0,-1,0), vector(0,-20,0)),
    ('D', rotate_face_double, change_d2, "D2", vector(0,-1,0), vector(0,-20,0)),
    # M, M', M2 18 19 20
    ('M', rotate_face_clk,  change_m,  "M",  vector(-1,0,0), vector(0,0,0)),
    ('M', rotate_face_aclk, change_mp, "M'", vector(-1,0,0), vector(0,0,0)),
    # ('M', rotate_face_double, change_m, "M2", vector(-1,0,0), vector(0,0,0)),
    # E, E', E2 21 22 23
    ('E', rotate_face_clk,  change_e,  "E",  vector(0,-1,0), vector(0,0,0)),
    ('E', rotate_face_aclk, change_ep, "E'", vector(0,-1,0), vector(0,0,0)),
    # ('E', rotate_face_double, change_e, "E2", vector(0,-1,0), vector(0,0,0)),
    # S, S', S2 24 25 26
    ('S', rotate_face_clk,  change_s,  "S",  vector(0,0,-1), vector(0,0,0)),
    ('S', rotate_face_aclk, change_sp, "S'", vector(0,0,-1), vector(0,0,0)),
    # ('S', rotate_face_double, change_s, "S2", vector(0,0,-1), vector(0,0,0)),
    # x, x', x2 27, 28, 29
    ('x', rotate_face_clk,  change_x,  "x",  vector(-1,0,0), vector(0,0,0)),
    ('x', rotate_face_aclk, change_xp, "x'", vector(-1,0,0), vector(0,0,0)),
    ('x', rotate_face_double, change_x2, "x2", vector(-1,0,0), vector(0,0,0)),
    # y, y', y2 30, 31, 32
    ('y', rotate_face_clk,  change_y,  "y",  vector(0,1,0),  vector(0,0,0)),
    ('y', rotate_face_aclk, change_yp, "y'", vector(0,1,0),  vector(0,0,0)),
    ('y', rotate_face_double, change_y2, "y2", vector(0,1,0),  vector(0,0,0)),
    # z, z', z2 33, 34, 35
    ('z', rotate_face_clk,  change_z,  "z",  vector(0,0,-1), vector(0,0,0)),
    ('z', rotate_face_aclk, change_zp, "z'", vector(0,0,-1), vector(0,0,0)),
    ('z', rotate_face_double, change_z2, "z2", vector(0,0,-1), vector(0,0,0)),
    # #  for wide moves 
    # # uw uw' uw2 36, 37, 38
    # ('u', rotate_face_clk, change_u, "u", vector(0,1,0),  vector(0,20,0)),
    # ('u', rotate_face_aclk, change_u, "u'", vector(0,1,0), vector(0,20,0)),
    # ('u', rotate_face_double, change_u, "u2", vector(0,1,0),  vector(0,20,20)),
    # # lw lw' lw2 39, 40, 41
    # ('l', rotate_face_clk, change_l, "l", vector(-1,0,0), vector(-20,0,0)),
    # ('l', rotate_face_aclk, change_l, "l'", vector(-1,0,0), vector(-20,0,0)),
    # ('l', rotate_face_double, change_l, "l2", vector(-1,0,0), vector(-20,0,0)),
    # # fw fw' fw2 42, 43, 44
    # ('f', rotate_face_clk, change_f, "f", vector(0,0,1),  vector(0,0,20)),      
    # ('f', rotate_face_aclk, change_f, "f'", vector(0,0,1),  vector(0,0,20)),
    # ('f', rotate_face_double, change_f, "f2", vector(0,0,1),  vector(0,0,20)),
    # # rw rw' rw2 45, 46, 47
    # ('r', rotate_face_clk, change_r, "r", vector(1,0,0),  vector(20,0,0)),  
    # ('r', rotate_face_aclk, change_r, "r'", vector(1,0,0),  vector(20,0,0)),
    # ('r', rotate_face_double, change_r, "r2", vector(1,0,0),  vector(20,0,0)),
    # # bw bw' bw2 48, 49, 50
    # ('b', rotate_face_clk, change_b, "b", vector(0,0,-1), vector(0,0,-20)),
    # ('b', rotate_face_aclk, change_b, "b'", vector(0,0,-1), vector(0,0,-20)),
    # ('b', rotate_face_double, change_b, "b2", vector(0,0,-1), vector(0,0,-20)),
    # # dw dw' dw2 51, 52, 53
    # ('d', rotate_face_clk, change_d, "d", vector(0,-1,0), vector(0,-20,0)),
    # ('d', rotate_face_aclk, change_d, "d'", vector(0,-1,0), vector(0,-20,0)),   
    # ('d', rotate_face_double, change_d, "d2", vector(0,-1,0), vector(0,-20,0)),
]
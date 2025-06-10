from vpython import *
cube=[]
rotatee=False
move_queue = []

for x in range(3):
    for y in range(3):
        for z in range(3):
            pos = vector(1.1*x-1.1,1.1*y-1.1,1.1*z-1.1)
            face = box(pos=pos, size=vector(1, 1, 1), color=color.white)
            if x==2: 
               p=box(pos=pos+vector(0.5, 0, 0), size=vector(0.01, 0.9, 0.9), color=color.red)
               cube.append(p)
            if x==0: 
               p=box(pos=pos-vector(0.5, 0, 0), size=vector(0.01, 0.9, 0.9), color=color.orange)
               cube.append(p)
            if y==2: 
               p=box(pos=pos+vector(0,0.5,0), size=vector(0.9, 0.01, 0.9), color=color.blue)
               cube.append(p)
            if y==0: 
               p=box(pos=pos-vector(0,0.5,0), size=vector(0.9, 0.01, 0.9), color=color.green)
               cube.append(p)
            if z==2: 
               p=box(pos=pos+vector(0, 0, 0.5), size=vector(0.9, 0.9, 0.01), color=color.white)
               cube.append(p)
            if z==0: 
               p=box(pos=pos-vector(0, 0, 0.5), size=vector(0.9, 0.9, 0.01), color=color.yellow)
               cube.append(p)
            cube.append(face)
def update_layers():
    global top,right,front,bottom,left,back
    top = [c for c in cube if round(c.pos.y, 1)>= 1.1 ]
    right = [c for c in cube if round(c.pos.x, 1) >=1.1 ]
    front = [c for c in cube if round(c.pos.z, 1) >=  1.1 ]
    bottom = [c for c in cube if round(c.pos.y, 1) <= -1.1 ]
    left = [c for c in cube if round(c.pos.x, 1) <=  -1.1 ]
    back = [c for c in cube if round(c.pos.z, 1) <= -1.1]
update_layers()
def rotate(cubef,axis,angle,origin):
   global rotatee
   rotatee = True
   for _ in range(25):
        rate(250)
        for c in cubef:
            c.rotate(axis=axis, angle=angle/50, origin=origin)
   update_layers()
   rotatee = False

   if move_queue:
        next= move_queue.pop(0)
        exec(next)
def exec(x):
    if x == 'j':
        rotate(top, vec(0, 1, 0), -pi, vec(0, 1.1, 0))
    elif x == 'l':
        rotate(bottom, vec(0, 1, 0), pi, vec(0, -1.1, 0))
    elif x == 'i':
        rotate(right, vec(1, 0, 0), -pi, vec(1.1, 0, 0))
    elif x == 'd':
        rotate(left, vec(1, 0, 0), pi, vec(-1.1, 0, 0))
    elif x == 'h':
        rotate(front, vec(0, 0, 1), -pi, vec(0, 0, 1.1))
    elif x == 'w':
        rotate(back, vec(0, 0, 1), pi, vec(0, 0, -1.1))
    if x == 'j':
        rotate(top, vec(0, 1, 0), -pi, vec(0, 1.1, 0))
    elif x == 'l':
        rotate(bottom, vec(0, 1, 0), pi, vec(0, -1.1, 0))
    elif x == 'i':
        rotate(right, vec(1, 0, 0), -pi, vec(1.1, 0, 0))
    elif x == 'd':
        rotate(left, vec(1, 0, 0), pi, vec(-1.1, 0, 0))
    elif x == 'h':
        rotate(front, vec(0, 0, 1), -pi, vec(0, 0, 1.1))
    elif x == 'w':
        rotate(back, vec(0, 0, 1), pi, vec(0, 0, -1.1))  pi
    elif x == 'f':
        rotate(top, vec(0, 1, 0), pi, vec(0, 1.1, 0))
    elif x == 's':
        rotate(bottom, vec(0, 1, 0), -pi, vec(0, -1.1, 0))
    elif x == 'k':
        rotate(right, vec(1, 0, 0), pi, vec(1.1, 0, 0))
    elif x == 'e':
        rotate(left, vec(1, 0, 0), -pi, vec(-1.1, 0, 0))
    elif x == 'g':
        rotate(front, vec(0, 0, 1), -pi, vec(0, 0, 1.1))
    elif x == 'o':
        rotate(back, vec(0, 0, 1), pi, vec(0, 0, -1.1))
    elif x == 'n' or x == 'b':
        rotate(cube, vec(1, 0, 0), pi, vec(1.1, 0, 0))
    elif x == 'y' or x == 't':
        rotate(cube, vec(1, 0, 0), -pi, vec(1.1, 0, 0))
    elif x == ';':
        rotate(cube, vec(0, 1, 0), -pi, vec(0, 1.1, 0))
    elif x == 'a':
       rotate(cube, vec(0, 1, 0), pi, vec(0, 1.1, 0)) 
    elif x == 'p':
        rotate(cube, vec(0, 0, 1), -pi, vec(0, 0, 1.1))
    elif x == 'q':
        rotate(cube, vec(0, 0, 1), pi, vec(0, 0, 1.1))
def keyInput(evt):
    s = evt.key.lower()
    if rotatee:
        move_queue.append(s)
    else:
        exec(s)
scene.bind('keydown', keyInput)

while True:
    rate(250)

from kociemba import solve
from cube_by_keys import *
from cube_by_not import *
from cube_by_color import *
from change_for_kociemba import *
from cube_scan import *
from solution import *
from pros import *

def print_cube(cube):
    # Unpack cube faces
    up, left, front, right, back, down = cube

    def row_to_str(row):
        return ' '.join(row)

    print()
    
    # cube[0] face (centered)
    for row in up:
        print("        " + row_to_str(row))
    
    print()  # Empty line between sections

    # LEFT, FRONT, RIGHT, BACK in a row
    for i in range(3):
        print(
            row_to_str(left[i]) + "   " +
            row_to_str(front[i]) + "   " +
            row_to_str(right[i]) + "   " +
            row_to_str(back[i])
        )
    
    print()  # Empty line between sections

    # DOWN face (centered)
    for row in down:
        print("        " + row_to_str(row))
    
    print()

print(" Welcome to rubicks cube Simulation")
print("PLease select from following options")

print("1 for Playing with 3d simulation")
print("2 for finding solution of the scrambled cube")

state = input("Type Here:")

if state == "1":
    rubiks_cube_simulator()
    exit()

elif state == "2":
    print("How do you want input the scramble")
    print("1.Scan Using Camera")
    print("2.Enter Scamble Using notations")
    print("3.By providing color of each face")

    state2 = input("Type Here:")
    if state2 == "1":
        color_map={
            0 : 'White',
            1 : 'Orange',
            2 : 'Green', 
            3 : 'Red',
            4 : 'Blue',
            5 : 'Yellow',
        }
        print("Do you want to us the deafult color scheme?")
        color_sch = input("Type Here(y/n):")
        if color_sch == "y" or color_sch == "Y":
            state = scan2()
        elif color_sch == "n" or color_sch == "N": 
            print("First window will appear in 3 seconds in which you have to give the color scheme of the cube by scanning each face center once")
            time.sleep(2)
            state = scan()
        required_state = change_for_kociemba(state)
        solution = solve(required_state)
        scramble = solution_of_scramble(solution)
        # print(solve(state))
        print("You can acieve the scramble by following moves:", scramble)
        print("You can solve the cube by following moves:", solution)

        print("The cube will be shown in the simulation window in 2 seconds for better perspective")
        time.sleep(2)
        rubiks_cube_solver_color(scramble,solution)
        #  print the cube state ``

    elif state2 =="2": 
        s_in = input("Type the Scramble:")
        scramble = tokenize_moves(s_in)
        sol = solution_of_scramble(s_in)
        print('solution:',sol)
        print("The cube will be shown in the simulation window  in 2 seconds")
        time.sleep(2)
        rubiks_cube_solver(scramble,sol)

    elif state2 =="3":
        color_map={
            0 : 'White',
            1 : 'Orange',
            2 : 'Green',
            3 : 'Red',
            4 : 'Blue',
            5 : 'Yellow',
        }
        print("Orient the cube with White centre in TOP and Green centre in FRONT")
        print("Enter the color of each face , W = White, Y = Yellow, G = Green, R = Red, B = Blue, O = Orange")
        cube_state = [[[None for _ in range(3)] for _ in range(3)] for _ in range(6)]
        state = ""
        for i in range(6):
            print("for the color:", color_map[i])
            for j in range(3):
                row = input("Enter the "+ str(j+1) + "th row of "+ color_map[i]+"  face:")
                
                cube_state[i][j][0] = row[0]
                cube_state[i][j][1] = row[2]
                cube_state[i][j][2] = row[4]
                state += row[0]+row[2]+row[4]
        required_state = change_for_kociemba(state)
        solution = solve(required_state)
        scramble = solution_of_scramble(solution)
        # print(solve(state))
        print("You can acieve the scramble by following moves:", scramble)
        print("You can solve the cube by following moves:", solution)

        print("The cube will be shown in the simulation window in few seconds for better perspective")
        time.sleep(5)
        rubiks_cube_solver_color(scramble,solution)
        #  print the cube state ``

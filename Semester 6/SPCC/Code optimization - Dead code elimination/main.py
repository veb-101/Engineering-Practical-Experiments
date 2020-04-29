# FINAL

import os
os.system("clear")


with open("test.txt") as f:
    lines = []
    lines = [i.replace("\n", "") for i in f.readlines()]


def used(variable, code):
    counts = 0
    for i in code:
        if variable in i:
            counts += 1
    return False if counts > 0 else True

def redefined_variables():
    pass

def dead_code_elimination(lines):
    variable = []
    expressions = []

    lines = [i.replace(" ", "") for i in lines]

    # print(lines)
    print("------------------------------")
    print("Original code...")
    for i in lines:
        print(i)


    for i in lines:
        left, right = i.split("=")
        variable.append(left)
        expressions.append(right)

    # print(variable)
    # print(expressions)
    # print(lines)

    # FIRST: REMOVING REDEFINED VARIABLES
    redefined_variables_line = []

    for i in range(len(variable)):
        if variable[i] in variable[i+1:]:
            redefined_variables_line.append(i)
    
    # print(redefined_variables_line)

    variable = [j for i, j in enumerate(variable) if i not in redefined_variables_line]
    expressions = [j for i, j in enumerate(expressions) if i not in redefined_variables_line]
    lines = [j for i, j in enumerate(lines) if i not in redefined_variables_line]

    # print(variable)
    # print(expressions)
    # print(lines)

    # SECOND: REMOVING SIMPLE ASSIGNMENT STATEMENTS NOT USED like x = 3
    dead_code = []
    dead_code_line = []

    for i in range(len(variable)):
        if len(expressions[i]) == 1:
            # print(variable[i], expressions[i+1:])
            if used(variable[i], expressions[i+1:]):
                # print(variable[i]+"="+expressions[i])
                dead_code.append((i, variable[i]+"="+expressions[i]))
                dead_code_line.append(i)

    # print("------------------------------")            
    # print("Dead code lines...")
    # for i in dead_code:
    #     print(f"Line: {i[0]+1}, code: {i[1]}")



    print("------------------------------")
    print("Removing dead code...")
    for i, j in enumerate(lines):
        if i in dead_code_line:
            continue
        else:
            print(j)
    

    lines = [j for i, j in enumerate(lines) if i not in dead_code_line]

    return lines


# for i in range(2):
#     print(f"PASS - {i}")
#     lines = dead_code_elimination(lines)
#     print()

dead_code_elimination(lines)
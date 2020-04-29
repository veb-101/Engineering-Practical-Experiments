'''
    author: Virag Dosani (@repl.it/@VTech1699)
'''

import sympy 
from sympy import * 

def readData(f):
    with open(f) as f:
        data = []
        da = f.read().split("\n")
        for line in da:
            data.append(line.split("="))
    
    return data


def algebraicSimplify(data):
    x,y,z = symbols('x y z')
    simplfy = []
    for i in data:
        expr = eval(i[1])
        smpl = simplify(expr)
        simplfy.append([i[0],expr, smpl])
    
    return simplfy


def printData(data):
    print("Input Code: ")
    for i in data:
        print(i[0]," = ",i[1]) 
    
    print("\nCode after Algebraic Simplification: ")
    for i in data:
        print(i[0]," = ",i[2])  

    return


if __name__ == '__main__':
    input = "input.txt"
    data = readData(input)
    output = algebraicSimplify(data)
    print("Algebraic Simplification")
    printData(output)


'''
OUTPUT:
Algebraic Simplification
Input Code: 
a   =  sin(x)**2 + cos(x)**2
b   =  (x**3 + x**2 - x - 1)/(x**2 + 2*x + 1)
c   =  gamma(x)/gamma(x - 2)
d   =  (x**2 + y**2 + z**2)/(-x**2 - y**2 - z**2)

Code after Algebraic Simplification: 
a   =  1
b   =  x - 1
c   =  (x - 2)*(x - 1)
d   =  -1
'''
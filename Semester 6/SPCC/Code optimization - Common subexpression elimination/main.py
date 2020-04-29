'''
    author: Virag Dosani (@repl.it/@VTech1699)
'''

import re
import os
os.system("clear")

def readData(f):
    with open(f) as source:
        data = source.readlines()
    
    return data


def createCode(data):
    expr_buffer = []
    code = []
    for line in data:
        print("=====",line)
        spline = line.replace(" ", "")
        if "=" in spline:
            expr = (re.findall(r"(\w)+=\S*", spline))
            for y in expr_buffer:
                print("Y: ",y)
                for x in y:
                    print("X: ",x)
                    if expr[0] == x:
                        # expr_buffer.remove(y)
                        print(expr[0],"==",x)
                        print("\nExpr_Buffer (=): ",expr_buffer)
                        print("spLine (=): ",spline)
                        print("Code (=): ",x,s)
        
        if "/" in spline:
            expr = (re.findall(r"[a-zAZ]+[\d]*/[a-zA-Z]+[\d]*", spline))
            for x in expr:
                if x not in expr_buffer:
                    expr_buffer.append(x)
                    s = "t" + str(expr_buffer.index(x))
                    code.append([s,x])
                    spline = spline.replace(x, s)
                    print("\nExpr_Buffer (/): ",expr_buffer)
                    print("spLine (/): ",spline)
                    print("Code (/): ",x,s)
                else:
                    s = "t" + str(expr_buffer.index(x))
                    spline = spline.replace(x, s)
                    print("\nExpr_Buffer (/): ",expr_buffer)
                    print("spLine (/): ",spline)
                    print("Code (/): ",x,s)

        if "*" in spline:
            expr = (re.findall(r"[a-zAZ]+[\d]*\*[a-zA-Z]+[\d]*", spline))
            for x in expr:
                if x not in expr_buffer:
                    expr_buffer.append(x)
                    s = "t"+ str(expr_buffer.index(x))
                    code.append([s,x])
                    spline = spline.replace(x, s)
                    print("\nExpr_Buffer (*): ",expr_buffer)
                    print("spLine (*): ",spline)
                    print("Code (*): ",x,s)
                else:
                    s = "t" + str(expr_buffer.index(x))
                    spline = spline.replace(x, s)
                    print("\nExpr_Buffer (*): ",expr_buffer)
                    print("spLine (*): ",spline)
                    print("Code (*): ",x,s)

        if "+" in spline:
            expr = (re.findall(r"[a-zAZ]+[\d]*\[a-zA-Z]+[\d]*", spline))
            for x in expr:
                if x not in expr_buffer:
                    expr_buffer.append(x)
                    s = "t"+ str(expr_buffer.index(x))
                    code.append([s,x])
                    spline = spline.replace(x, s)
                    print("\nExpr_Buffer (+): ",expr_buffer)
                    print("spLine (+): ",spline)
                    print("Code (+): ",x,s)
                else:
                    s = "t" + str(expr_buffer.index(x))
                    spline = spline.replace(x, s)
                    print("\nExpr_Buffer (+): ",expr_buffer)
                    print("spLine (+): ",spline)
                    print("Code (+): ",x,s)
        
        if "-" in spline:
            expr = (re.findall(r"[a-zAZ]+[\d]*-[a-zA-Z]+[\d]*", spline))
            for x in expr:
                if x not in expr_buffer:
                    expr_buffer.append(x)
                    s = "t"+ str(expr_buffer.index(x))
                    code.append([s,x])
                    spline = spline.replace(x, s)
                    print("\nExpr_Buffer (-): ",expr_buffer)
                    print("spLine (-): ",spline)
                    print("Code (-): ",x,s)
                else:
                    s = "t" + str(expr_buffer.index(x))
                    spline = spline.replace(x, s)
                    code.append(spline)
                    print("\nExpr_Buffer (-): ",expr_buffer)
                    print("spLine (-): ",spline)
                    print("Code (-): ",x,s)
    print()
    
    return code


def displayCode(data):
    for i in data:
        print(i[0]," = ",i[1], end="\n")
        
    return


if __name__ == '__main__':
    input = "input3.txt"
    data = readData(input)
    print("Input Expressions:")
    code = createCode(data)
    print("\nBefore Optimization: ")
    displayCode(code)

# COA final project
# Number base conversion
# base2-base36 conversion
# generates Excess-3 and Grey code
import string
from math import modf as mf
from tkinter import Tk, messagebox, Label, Entry, Button

ref = string.digits + string.ascii_uppercase
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")


def helper(num):
    fractional = []
    num = num.split(".")
    integer = [str(ref.index(num[0][i])) for i in range(len(num[0]))]
    if len(num) > 1:
        fractional = [str(ref.index(num[1][i])) for i in range(len(num[1]))]
    return integer, fractional


def check(number, base):
    base = int(base)
    for i in number:
        if i == ".":
            pass
        else:
            x = ref.index(i)
            if int(x) >= base:
                return False
    return True


def fetch():
    if check(num.get(), numBase.get()):
        number = num.get()
        numbase = int(numBase.get())
        basee = int(base.get())
        if numbase == 10:
            intermediate_value = int(number) if number.isdecimal() else float(number)
            value = decimal_to_any(intermediate_value, basee)
        else:
            value = others_to_decimal(number, numbase, basee)

        excess_3_value = to_excess_3(number, numbase)
        grey_value = helper_grey_code(number, numbase)

        label_5["text"] = str(value) + str(basee).translate(SUB)
        label_7["text"] = str(excess_3_value)
        label_9["text"] = str(grey_value)

    else:
        messagebox.showerror("Base Error", "Enter correct number")


def ExitApplication():
    MsgBox = messagebox.askquestion(
        'Exit Application', 'Are you sure you want to exit the application', icon='warning')
    if MsgBox == 'yes':
        root.destroy()


def decimal_to_any(num, base):
    fractional = False
    if isinstance(num, float):
        points = 5
        num = [int(i) for i in str(num).split(".")]
        integer = num[0]
        length = len(str(num[1]))
        fractional = float(str("0.") + str(num[1]))
    else:
        integer = num
    ans = ""
    # Decimal part conversion
    while integer != 0:
        intermediate = integer % base
        intermediate = ref[intermediate]
        ans = str(intermediate) + ans
        integer //= base

    # Floating part conversion
    if fractional:
        ans += "."
        while points:
            fractional, i = mf(fractional * base)
            fractional = round(fractional, length)
            i = ref[int(i)]
            ans += i
            points -= 1
    return ans


def others_to_decimal(num, numBase, base):
    integer, fractional = helper(num)
    # Conversion
    ans = 0
    integer = integer[::-1]
    i = len(integer) - 1
    while i >= 0:
        ans += (int(integer[i]) * numBase**i)
        i -= 1

    if fractional:
        multiList = list(range(-1, -len(fractional) - 1, -1))
        i = 0
        while i < len(fractional):
            ans += (int(fractional[i]) * numBase**(multiList[i]))
            i += 1
    if base == 10:
        return ans
    return decimal_to_any(ans, base)


def binary_to_gray(num):
    integer, fractional = helper(num)
    ans = []
    ans.append(int(integer[0]))
    for i in range(len(integer) - 1):
        ans.append(int(integer[i]) ^ int(integer[i + 1]))

    if fractional:
        fractional.append("0")
        ans.append(".")
        ans.append(int(fractional[0]))
        for i in range(len(fractional) - 1):
            ans.append(int(fractional[i]) ^ int(fractional[i + 1]))
    return "".join([str(i) for i in ans])


def helper_grey_code(number, number_base):
    grey_code_value = others_to_decimal(number, number_base, 2)
    # print(f"Binary equivalent: {grey_code_value}")
    return binary_to_gray(grey_code_value)


def to_excess_3(num, numbase):
    number = others_to_decimal(num, numbase, 10)
    number += 3
    ans = decimal_to_any(number, numbase)
    return ans

# def grey_to_binary(num):
#     integer, fractional = helper(num)
#     ans = []
#     ans.append(int(integer[0]))
#     for i in range(1, len(integer)):
#         ans.append(ans[-1] ^ int(integer[i]))

#     if fractional:
#         fractional.append("0")
#         ans.append(".")
#         ans.append(int(fractional[0]))
#         for i in range(1, len(fractional)):
#             ans.append(ans[-1] ^ int(fractional[i]))
#     return "".join([str(i) for i in ans])


if __name__ == '__main__':
    root = Tk()
    label_1 = Label(root, text="    Number ")
    label_2 = Label(root, text="Number base")
    label_3 = Label(root, text="Convert to ")
    label_6 = Label(root, text="  Excess-3 ")
    label_7 = Label(root, text="        ")
    label_8 = Label(root, text=" Grey code ")
    label_9 = Label(root, text="        ")
    label_4 = Label(root, text=" Converted ")
    label_5 = Label(root, text="        ")

    label_1.grid(row=0, column=0)
    label_2.grid(row=1, column=0)
    label_3.grid(row=2, column=0)
    label_4.grid(row=5, column=0)
    label_5.grid(row=5, column=1)
    label_6.grid(row=3, column=0)
    label_7.grid(row=3, column=1)
    label_8.grid(row=4, column=0)
    label_9.grid(row=4, column=1)
    num = Entry(root)
    numBase = Entry(root)
    base = Entry(root)
    num.grid(row=0, column=1)
    numBase.grid(row=1, column=1)
    base.grid(row=2, column=1)

    Button(root, text="Convert", width=9, command=fetch).grid(row=2, column=2)
    Button(root, text="Close", width=9, command=ExitApplication).grid(row=3, column=2)
    root.geometry("+500+250")
    root.title("Base Conversion")
    root.mainloop()

# http://www.unitconversion.org/unit_converter/numbers-ex.html
# crosscheck Ans

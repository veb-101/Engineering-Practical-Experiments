import os
os.system("clear")


with open("test.txt") as f:
    lines = []
    lines = [i.replace("\n", "") for i in f.readlines()]

lines = [i.replace(" ", "") for i in lines]

print("------------------------------")
print("Original code...")
for i in lines: 
    print(i)


# find loop variable and update count
variable = []
expressions = []

for i, j in enumerate(lines):
    try:
        left, right = j.split("=")
        variable.append((i, left))
        expressions.append((i, right))
    except:
        pass

# print(expressions)

loop_variable = variable[0][1]
update_variable = variable[1][1]

if expressions[1][1][-1].isdigit():
    update_count = int(expressions[1][1][-1])


# get count multiplied with And loop count

for i in lines:
    if "<" in i:
        start = i.find("<") + 1
        end = i.find(")")
        loop_count = int(i[start:end])
        
# print(loop_count, loop_variable, update_count)

# define dummy variable 
dummy_variable = f"t = {update_count}"

# use dummy variable for loop 
dummy_in_loop = f"t = t + {update_count}"

loop_count_update = f"t<{loop_count * update_count}"

# print(dummy_variable, dummy_in_loop)
# print(expressions)
# print(list(loop_count_update))

# replace where loop variable used
replacing_  = list(expressions.pop())
replacing_[1] = "t"
# print(replacing_)
expressions.append(tuple(replacing_))
# print(expressions)

lines.insert(1, dummy_variable)
lines.insert(len(lines)-1, dummy_in_loop)

# update loop variable
line = lines[:]


for i, j in enumerate(lines):
    if "<" in j:
        j = list(j)
        start = j.index("<") - 1
        end = j.index(")")
        j[start: end] = list(loop_count_update)
        j = "".join(j)

        line[i] = j
    
    if "y" in j:
        j = list(j)
        start = j.index("=") + 1
        j[start:] = "t"
        j = "".join(j)
        line[i] = j


# print(expressions)


print("------------------------------")
print("Updated code...")
for i in line: 
    print(i)
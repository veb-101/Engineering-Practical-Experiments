# import string
def readData(f):
    with open(f) as t:
        data = []
        da = t.read().split("\n")
        for line in da:
            if len(line) != 0:
                data.append(line.split())
    return data


def create_MDT_MNT(data):
    mdt = []
    mnt = []
    mdtc,mntc = 0,0
    flag = 0
    temp = None
    for i, j in enumerate(data):
        if flag == 1:
            if len(j) == 2 and temp != 1:
                j[1] = j[1].replace('&arg','#')            
            mdt.append([mdtc,j])
            mdtc += 1
        
        if temp:
            mnt.append([mntc,j[0],mdtc-1])
            mntc += 1
            temp=0

        if j[0].lower() == 'macro':
            flag = temp = 1
        
        if j[0].lower() == 'mend':
            flag = 0
    return mdt, mnt


def expand_Macro(data, mnt, mdt):
    output = []
    lines = []

    for i, j in enumerate(data):
        for k in mnt:
            if j[0] == k[1] and data[i-1][0] != 'MACRO':
                arg = j[1].split(',')
                ind = k[2]
                temp = mdt[ind:]   
                for l in temp:
                    if l[1][0] == 'MEND':
                        break
                    if j[0] == k[1]:
                        if l[1][0] != j[0]:
                            aIndex = l[1][1].find('#')
                            aIndex = int(l[1][1][aIndex+1])-1
                            old = l[1][1].split(',')[1]
                            l[1] = [l[1][0], l[1][1].replace(old,arg[aIndex])]
                            lines.append(l[1])                            
                            output.append(l[1])
        if len(lines):
            pass
        else:
            output.append(j)
        lines.clear()
    
    return output


def printData(data):
    for i, j in enumerate(data):
        print(i, end = "\t")
        for k in j:
            print(k, end = " ")
        print()
    return


if __name__ == '__main__':
    data = readData('Exp4.txt')
    mdt, mnt = create_MDT_MNT(data)

    print("\nMacro Program")    
    printData(data)
    print("\nMDT")
    for i in mdt:
        print(i)
    print("\nMNT")
    for i in mnt:
        print(i)
    print()

    output = expand_Macro(data, mnt, mdt)
    print("\nExpanded Macro Program")
    printData(output)
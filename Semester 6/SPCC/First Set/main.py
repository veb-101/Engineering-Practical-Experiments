'''
    author: Virag Dosani (@VTech1699)
'''

# First Set

from collections import OrderedDict


def readRules(f):
    with open(f) as t:
        rules = []
        for line in t:
            rules.append(line.replace(" ","").strip().split('\n'))

    return rules

def non_term_appender(firsts, firsts_dict, rules):
    for rule in rules:
        if rule[0][0] not in firsts:
            firsts.append(rule[0][0])
            firsts_dict[rule[0][0]] = []
    
    return firsts, firsts_dict, rules


def create_Firsts(rules):
    firsts = []
    rules_dict = OrderedDict()
    firsts_dict = OrderedDict()
    
    number_of_rules = len(rules)
    rule_count = first_count = 0
    firsts, firsts_dict, rules = non_term_appender(firsts, firsts_dict, rules)
    for first in firsts:
        rules_dict[first] = rules[rule_count][0][3:]
        rule_count += 1

    for rule in rules:
        if rule[0][3].islower():
            firsts_dict[rule[0][0]].extend(rule[0][3])
    for rule in rules:
        if rule[0][3].isupper():
            firsts_dict[rule[0][0]].extend(firsts_dict[rule[0][3]])

    return firsts_dict


def write_File(firsts_dict, output):
    with open(output, "w+") as wp:
        for k in firsts_dict:
            wp.write("First (%s): " % k)
            wp.write("%s\n" % firsts_dict[k])
    
    return

def display_File(f):
    with open(f) as fp:
        for line in fp:
            print(line.strip())
        print()
    
    return


if __name__ == '__main__':
    input, output = "input.txt","firsts.txt"
    rules = readRules(input)
    firsts = create_Firsts(rules)
    write_File(firsts, output)
    
    print("First Set from given Grammar")
    print("Input Grammar")
    display_File(input)
    print("First Set")
    display_File(output)


'''
OUTPUT:
input.txt, firsts.txt
First Set from given Grammar
Input Grammar
S -> ABCD
A -> b
A -> x
B -> c
C -> d
D -> e

First Set
First (S): ['b', 'x']
First (A): ['b', 'x']
First (B): ['c']
First (C): ['d']
First (D): ['e']

input2.txt, firsts2.txt
First Set from given Grammar
Input Grammar
S -> Bb
S -> Cd
B -> aB
B -> o
C -> cC
C -> o

First Set
First (S): ['a', 'o', 'c', 'o']
First (B): ['a', 'o']
First (C): ['c', 'o']
'''
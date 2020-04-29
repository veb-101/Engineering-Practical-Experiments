'''
    author: Virag Dosani (@VTech1699)
'''

# Follow Set
from collections import OrderedDict


def readRules(f):
    with open(f) as t:
        rules = []
        for line in t:
            rules.append(line.replace(" ","").strip().split('\n'))

    return rules


def non_term_appender(firsts, firsts_dict, follow_dict, rules):
    for rule in rules:
        if rule[0][0] not in firsts:
            firsts.append(rule[0][0])
            firsts_dict[rule[0][0]] = []
            follow_dict[rule[0][0]] = []
    
    return firsts, firsts_dict, follow_dict, rules


def create_Follow(rules):
    firsts = []
    rules_dict = OrderedDict()
    firsts_dict = OrderedDict()
    follow_dict = OrderedDict()
    
    number_of_rules = len(rules)
    rule_count = first_count = 0
    firsts, firsts_dict, follow_dict, rules = non_term_appender(firsts, firsts_dict, follow_dict, rules)

    for first in firsts:
        rules_dict[first] = rules[rule_count][0][3:]
        rule_count += 1
    for rule in rules:
        if rule[0][3].islower():
            firsts_dict[rule[0][0]].extend(rule[0][3])
    for rule in rules:
        if rule[0][3].isupper():
            firsts_dict[rule[0][0]].extend(firsts_dict[rule[0][3]])

    rules_keys = list(rules_dict.keys())
    key_count = len(rules_keys)
    
    for k in rules_dict:
        tmp_rule_str = rules_dict[k]
        if k == rules_keys[0]:
            follow_dict[k].append('$')
        for i in range(key_count):
            if rules_keys[i] in tmp_rule_str:
                tmp_rule_list = list(tmp_rule_str)
                current_non_term_index = tmp_rule_list.index(rules_keys[i])

                if current_non_term_index == (len(tmp_rule_list) - 1):
                    follow_dict[rules_keys[i]].extend(follow_dict[rules_keys[0]])
                else:
                    follow_dict[rules_keys[i]].extend(
                        firsts_dict[rules_keys[(i + 1) % key_count]])

    return follow_dict


def write_File(follow_dict, output):
    with open(output, "w+") as wp:
        for k in follow_dict:
            wp.write("Follow (%s): " % k)
            wp.write("%s\n" % follow_dict[k])
    
    return

def display_File(f):
    with open(f) as fp:
        for line in fp:
            print(line.strip())
        print()
    
    return


if __name__ == '__main__':
    input, output = "input2.txt","follow2.txt"
    rules = readRules(input)
    follow = create_Follow(rules)
    write_File(follow, output)
    
    print("Follow Set from given Grammar")
    print("Input Grammar")
    display_File(input)
    print("Follow Set")
    display_File(output)


'''
OUTPUT:
input.txt, firsts.txt
Follow Set from given Grammar
Input Grammar
S -> ABCD
A -> a
A -> b
B -> c
C -> d
D -> e

Follow Set
Follow (S): ['$']
Follow (A): ['c']
Follow (B): ['d']
Follow (C): ['e']
Follow (D): ['$']

input2.txt, firsts2.txt
Follow Set from given Grammar
Input Grammar
S -> Bb
S -> Cd
B -> aB
B -> o
C -> cC
C -> o

Follow Set
Follow (S): ['$']
Follow (B): ['c', 'o', '$']
Follow (C): ['a', 'o', 'c', 'o']
'''
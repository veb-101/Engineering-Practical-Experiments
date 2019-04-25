# for proper examples refer https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
# https://www.youtube.com/watch?v=V5-7GzOfADQ

# uncomment print statements to see how the table is updated


def prefixTable(pattern):
    prefix_table = [0]

    for i in range(1, len(pattern)):
        j = prefix_table[i-1]
        # print(f"(i,j): {i, j}")

        while(j > 0 and pattern[j] != pattern[i]):
            # print(f"In while j values: {j}, table[{j}]: {prefix_table[j-1]}, Pattern[{j}]: {pattern[j]}, Pattern[{i}]: {pattern[i]}")
            j = prefix_table[j-1]
        # print(f"J: {j}, Pattern[{j}]: {pattern[j]}, Pattern[{i}]: {pattern[i]}")
        prefix_table.append(j+1 if pattern[j] == pattern[i] else j)
        # print(f"Table: {prefix_table}")
        # print()
    return prefix_table


print(prefixTable("abadab"))


def kmp(text, pattern):
    table, ret, j = prefixTable(pattern), [], 0
    print(table)
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = table[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            ret.append(i - j + 2)
            j = table[j - 1]
    return ret


print(kmp("badbabababadaa", "ababada"))

# Time complexity:O(m+n)

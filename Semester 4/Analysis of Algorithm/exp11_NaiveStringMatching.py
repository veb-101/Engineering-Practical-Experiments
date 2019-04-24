# remove comments to optimize execution
def naiveStringMatching(pattern, txt):
    M = len(pattern)
    N = len(txt)
    count = 0
    i = 0
    indexes = []
    while i <= N-M:
        count = 0
        for j in range(M):
            if txt[i+j] != pattern[j]:
                break
            else:
                count += 1

        if count == M:
            indexes.append(i + 1)
            # i += M
        # elif count == 0:
        #     i = i + 1
        # else:
        #     i = i + count
        i += 1
    return indexes


if __name__ == '__main__':
    text = input("Enter text: ")
    pattern = input("Enter Pattern: ")
    positions = naiveStringMatching(pattern, text)
    if len(positions) > 0:
        for i in positions:
            print(f"Pattern found at position: {i}")
    else:
        print("Pattern not found")

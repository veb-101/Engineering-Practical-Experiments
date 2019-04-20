def rabinKarp(text, pat, pn):
    len_pn = len(pat)
    fingerprint_pattern = int(pat) % pn
    indexes = []
    for i in range(len(text) - len_pn + 1):
        curr = text[i: i + len_pn]
        if int(curr) % pn == fingerprint_pattern:
            if helperMatch(curr, pat):
                # print(f"found at position: {i + 1}")
                indexes.append(i+1)
    return indexes


def helperMatch(comb, pat):
    match = 0
    for i, j in enumerate(comb):
        if j == pat[i]:
            match += 1
    return match == len(pat)


if __name__ == '__main__':
    # digit input
    text = input("Enter text: ")
    pattern = input("Enter pattern: ")
    pn = 13  # any prime number
    positions = rabinKarp(text, pattern, pn)
    if len(positions) > 0:
        for i in positions:
            print(f"found at position: {i + 1}")
    else:
        print(f"pattern not found")

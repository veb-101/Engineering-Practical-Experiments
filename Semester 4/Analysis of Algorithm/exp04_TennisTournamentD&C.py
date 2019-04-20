def matchWinner(array, low, high):
    if low == high:
        return array[low]
    elif low == high - 1:
        if array[low] < array[high]:
            win = array[high]
        else:
            win = array[low]
        print(f"Winner between player {low} and player {high} is player {getIndex(win)}")
        return win
    else:
        mid = (low + high)//2
        w1  = matchWinner(array, low, mid)
        w2 = matchWinner(array, mid + 1, high)
        win = w1 if w1 > w2 else w2
        print(f"Winner between player {getIndex(w1)} and player {getIndex(w2)} is player {getIndex(win)}")
        return win
def getIndex(value):
    return ref.index(value)

if __name__ == "__main__":
    numofPlayers = int(input("Enter number of players: "))
    players = [int(input(f"Enter score for player {i+1}: ")) for i in range(numofPlayers)]
    print("\n---------SCORES--------")
    for i, j in enumerate(players, 1):
        print(f"Player {i} score: {j}")
    players.insert(0, 0)
    ref = players[:]
    print()
    finalWinner = matchWinner(players, 1, numofPlayers)
    print(f"\nFinal winner is player: {getIndex(finalWinner)} ")
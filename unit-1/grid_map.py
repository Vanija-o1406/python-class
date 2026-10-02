obstacles = [(2, 3), (1, 7), (5, 5)]

for i in range(8):
    for j in range(8):
        if (i, j) in obstacles:
            print("X", end=" ")
        else:
            if (i, j) == (0, 0):
                print("S", end=" ")
            elif (i, j) == (7, 7):
                print("G", end=" ")
            else:
                print(".", end=" ")
    print()
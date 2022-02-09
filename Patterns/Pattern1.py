"""
WRP to print patterns liske
1 2 3 4 5 6 7
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
1 2 3 4 5 6 7
"""

colms = 7

for row in range(0, colms):
    printValue = 1
    for column in range(colms - row, 0, -1):
        print(printValue, end=' ')
        printValue += 1
    print()

for row in range(1, colms):
    printValue = 1
    for column in range(row + 1):
        print(printValue, end=' ')
        printValue += 1
    print()

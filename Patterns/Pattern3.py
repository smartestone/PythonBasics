"""
WRP to print patterns like
  1   2   3   4   5   6   7
    2   3   4   5   6   7
      3   4   5   6   7
        4   5   6   7
          5   6   7
            6   7
              7
            6   7
          5   6   7
        4   5   6   7
      3   4   5   6   7
    2   3   4   5   6   7
  1   2   3   4   5   6   7

"""

rows = 7

for num in range(0, rows):

    for item in range(1, rows + 1):
        if item <= num:
            print(' ', end=' ')
        else:
            print(' ', item, end=' ')
    print()

for num in range(1, rows):

    for item in range(1, rows + 1):
        # print(item, end=' ')
        if item < (rows - num):
            print(' ', end=' ')
        else:
            print(' ', item, end=' ')
    print()

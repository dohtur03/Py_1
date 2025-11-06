x = 0

field = [[1,1,1,1],
         [1,1,1,1],
         [1,9,1,1]]

checker = [[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]

mover = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

x_max = len(field[0]) - 1
y_max = len(field) - 1

x = x_max
y = y_max
result = 0

for hor in range(x_max, -1, -1):
    for ver in range (y_max, -1, -1):
        if (ver + 1 > y_max and hor + 1 <= x_max):
            checker[ver][hor] = (field[ver][hor] + checker[ver][hor + 1])
            mover[ver][hor] = 1
        elif (ver + 1 <= y_max and hor + 1 > x_max):
            checker[ver][hor] = (field[ver + 1][hor] + checker[ver + 1][hor])
            mover[ver][hor] = 2
        elif (ver + 1 <= y_max and hor + 1 <= x_max):
            if (checker[ver][hor] + field[ver][hor + 1] + checker[ver][hor + 1]) > (checker[ver][hor] + field[ver + 1][hor] + checker[ver + 1][hor]):
                checker[ver][hor] = (field[ver][hor + 1] + checker[ver][hor + 1])
                mover[ver][hor] = 1
            else: 
                checker[ver][hor] = (field[ver + 1][hor] + checker[ver + 1][hor])
                mover[ver][hor] = 2

for rows in checker:
    print(*rows)

for rows in mover:
    print(*rows)



import numpy as np
x_size = 30
y_size = 10

field = np.random.randint(1, 10, size = (y_size, x_size))
checker = np.zeros((y_size, x_size), dtype = int)
mover = np.full((y_size, x_size), '!', dtype=str)   


#field = [[1,1,1,1],
#         [1,1,1,1],
#         [1,9,1,1]]

#checker = [[0,0,0,0],
#           [0,0,0,0],
#           [0,0,0,0]]

#mover = [[0,0,0,0],
#         [0,0,0,0],
#         [0,0,0,0]]

x_max = len(field[0]) - 1
y_max = len(field) - 1

x = x_max
y = y_max
result = 0

for hor in range(x_max, -1, -1):
    for ver in range (y_max, -1, -1):
        if (ver + 1 > y_max and hor + 1 <= x_max):
            checker[ver][hor] = (field[ver][hor] + checker[ver][hor + 1])
            mover[ver][hor] = ">"
        elif (ver + 1 <= y_max and hor + 1 > x_max):
            checker[ver][hor] = (field[ver + 1][hor] + checker[ver + 1][hor])
            mover[ver][hor] = "V"
        elif (ver + 1 <= y_max and hor + 1 <= x_max):
            if (checker[ver][hor] + field[ver][hor + 1] + checker[ver][hor + 1]) > (checker[ver][hor] + field[ver + 1][hor] + checker[ver + 1][hor]):
                checker[ver][hor] = (field[ver][hor + 1] + checker[ver][hor + 1])
                mover[ver][hor] = ">"
            else: 
                checker[ver][hor] = (field[ver + 1][hor] + checker[ver + 1][hor])
                mover[ver][hor] = "V"

for rows in field:
    print(*rows)
print("\n")
for rows in checker:
    print(*rows)
print("\n")
for rows in mover:
    print(*rows)



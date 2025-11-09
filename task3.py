lines = []
analyzer = []

with open ('input.txt', 'r') as file:
    line = file.readline()
    while line:
        line = line.strip().split()
        lines.append(line)
        line = file.readline()

mtx_rows = len(lines)
mtx_cols = len(lines[1])

for i in range(mtx_rows):
    row = []
    for j in range(mtx_cols):
        row.append(0)
    analyzer.append(row)

for line in lines:
    print(*line)

print("")

for rows in range(mtx_rows):
    for cols in range(mtx_cols):
        if int(lines[rows][cols]) == 0:
            analyzer[rows][cols] = 0
        else:
            near = [(rows-1, cols), (rows, cols-1), (rows-1, cols-1)]
            val = [analyzer[x][y] for x, y in near if x >= 0 and y >= 0 and analyzer[x][y] >= 0]
            analyzer[rows][cols] = min(val) + 1 if val else 1

for line in analyzer:          
       print(*line)
    


# HOW TO FIND A SQUARE AND A RING?

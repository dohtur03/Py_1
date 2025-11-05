num = 1
lines = [[num]]
for rows in range(1, 20):
    line = []
    for clmns in range(rows + 1):
        if 0 < clmns < len(lines[rows - 1]):
            num = lines[rows - 1][clmns] + lines[rows - 1][clmns - 1]
        else:
            num = 1
        line.append(num)
    lines.append(line)

for lns in lines:
    print(*lns)
        

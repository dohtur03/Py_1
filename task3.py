lines = []
with open ('input.txt', 'r') as file:
    line = file.readline()
    while line:
        line = line.strip()
        lines.append(line)
        line = file.readline()

print(lines)

# HOW TO FIND A SQUARE AND A RING?

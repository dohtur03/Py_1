import sys

all_lines = []
all_coords = []
counter = 0
vectors = 2
result = 0

for coords in sys.stdin:
    all_lines.append(coords)
    counter += 1
    if counter == vectors:
        break

for line in all_lines:
    vector = []
    numbers = line.split()
    for number in numbers:
        n = float(number)
        vector.append(n)
    all_coords.append(vector)

lines = len(all_coords) - 1
points = len(all_coords[0])
for i in range(lines):
    for j in range(points):
        the_num = all_coords[i][j] * all_coords[i+1][j]
        sys.stdout.write(str(the_num) + ' ')
        result += the_num
    sys.stdout.write(f"{the_num}\n")

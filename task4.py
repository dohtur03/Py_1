# Output N first rows of Pascal's triangle by the given number N of rows

def main():
    num = check_int()
    if num <= 0:
        print("Input must be a single positive int.")
    else:
        triangler(num)

# Check input for positive int
def check_int():
    try:
        num = int(input())
    except ValueError:
        num = -1
    return num

# Generate N raws of Pascal's trianlgle
def triangler(num): 
    lines = [[1]]
    for row in range(1, num):
        line = []
        for col in range(row + 1):
            if 0 < col < len(lines[row - 1]):
                val = lines[row - 1][col] + lines[row - 1][col - 1]
            else:
                val = 1
            line.append(val)
        lines.append(line)

    for line in lines:
        print(*line)
       
if __name__ == "__main__":
    main()

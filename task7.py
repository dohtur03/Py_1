# Finds the maximum sum of numbers in a matrix of numbers. Move only right and down along the matrix.

def main():
    field, saver, y, x = mapper()
    result = analyzer(field, saver, y, x)
    print(result)

def mapper():
# Input number of rows and columns + rows of numbers 
    y, x = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(y)]
    
# Generate a matrix to save results of the field's analysis
    saver = [[0] * x for _ in range(y)]
    saver[0][0] = field[0][0]
    return (field, saver, y, x)
    
# Fill the generated matrix with results of calculations (max sum and direction)
def analyzer(field, saver, y, x):    
    for col in range(1, x):
        saver[0][col] = saver[0][col - 1] + field[0][col]
    
    for row in range(1, y):
        saver[row][0] = saver[row - 1][0] + field[row][0]
    
    for row in range(1, y):
        for col in range(1, x):
            saver[row][col] = field[row][col] + max(saver[row - 1][col], saver[row][col - 1])
    
    return (saver[y - 1][x - 1])

if __name__ == "__main__":
    main()

def read_matrix(fname):
    error = False
    matrix = []
    try:
        with open(fname, 'r') as f:
            for line in f:
                line = line.strip()
                if line == '':
                    continue
                parts = line.split()
                matrix.append([int(x) for x in parts])
    except Exception as e:
        error = True
    return matrix, error

def dfs(matrix, visited, r, c, bounds, count):
    rows = len(matrix)
    cols = len(matrix[0])
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return
    if visited[r][c] or matrix[r][c] == 0:
        return
    visited[r][c] = True
    count[0] += 1
    # Update bounds: min_r, max_r, min_c, max_c
    if r < bounds[0]: bounds[0] = r
    if r > bounds[1]: bounds[1] = r
    if c < bounds[2]: bounds[2] = c
    if c > bounds[3]: bounds[3] = c
    # Visit neighbors (no diagonals)
    dfs(matrix, visited, r-1, c, bounds, count)
    dfs(matrix, visited, r+1, c, bounds, count)
    dfs(matrix, visited, r, c-1, bounds, count)
    dfs(matrix, visited, r, c+1, bounds, count)

def analyze_figure(bounds, count):
    height = bounds[1] - bounds[0] + 1
    width = bounds[3] - bounds[2] + 1
    area = height * width
    if area == count:
        # Perfect rectangle, call it square as per the problem
        return 'square'
    else:
        # Otherwise, circle
        return 'circle'

def find_figures(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0, 0
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False]*cols for _ in range(rows)]
    squares = 0
    circles = 0
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1 and not visited[r][c]:
                bounds = [r, r, c, c]  # min_r, max_r, min_c, max_c
                count = [0]  # using list to pass by reference
                dfs(matrix, visited, r, c, bounds, count)
                # ignore one-unit figures (problem says more than one unit)
                if count[0] <= 1:
                    continue
                kind = analyze_figure(bounds, count[0])
                if kind == 'square':
                    squares += 1
                else:
                    circles += 1
    return squares, circles

def main():
    matrix, err = read_matrix('input.txt')
    if err:
        print("0 0")
        return
    sq, cir = find_figures(matrix)
    print(sq, cir)

if __name__ == "__main__":
    main()


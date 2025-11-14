# Calculates the scalar product of two vectors in three dimensional space

vectors = 2

def main():
    all_lines = input_txt(vectors)
    all_coords = process_txt(all_lines)
    result = calc_vectors(all_coords)
    print(result)

# Input coordinates (3 points of 2 vectors)
def input_txt(vectors):
    all_lines = []
    counter = 0
    while counter < vectors:
        coords = input()
        all_lines.append(coords)
        counter += 1
    return all_lines

# Process input - separate into floats        
def process_txt(all_lines):
    all_coords = []
    for line in all_lines:
        vector = []
        numbers = line.split()
        for number in numbers:
            n = float(number)
            vector.append(n)
        all_coords.append(vector)
    return all_coords

# Calculate the scalar sum
def calc_vectors(all_coords):
    result = 0
    lines = len(all_coords) - 1
    points = len(all_coords[0])
    for i in range(lines):
        for j in range(points):
            the_num = all_coords[i][j] * all_coords[i+1][j]
            result += the_num
    return result 

if __name__ == "__main__":
       main()

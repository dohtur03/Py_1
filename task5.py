# Convert a string to a real number as if it were processed by the float() function and multiply by 2

def main():
    inp = input().strip()
    err, point = errors(inp)
    if err:
        print("Incorrect input")
        exit(1)
    num = floater(inp, point)
    print(f"{num * 2:.3f}")

# Check for the correct input
def errors(inp):
    err = False
    point = -1
    lngth = len(inp)
    
    if lngth == 0:
        err = True
        return err, point
    
    start = 0
    if inp[0] in ['-', '+']:
        start = 1

    pointed = 0
    for i in range(start, lngth):
        if not ('0' <= inp[i] <= '9'):
            if inp[i] == '.' and pointed == 0:
                pointed = 1
                point = i
            else:
                err = True
                break

    if lngth == start:
        err = True

    return err, point

# Process input and calculate the result
def floater(num, point):
    first = 0
    lngth = len(num)
    is_negative = False
    if num.startswith('-'):
        is_negative = True
        first = 1
    elif num.startswith('+'):
        first = 1

    digits = []
    for c in num[first:]:
        if c != '.':
            digits.append(int(c))

    part_len = 0
    if point != -1:
        part_len = lngth - point - 1

    result = 0
    for digit in digits:
        result = result * 10 + digit
    if part_len > 0:
        result = result / (10 ** part_len)
    if is_negative:
        result = -result
    return result

if __name__ == "__main__":
    main()

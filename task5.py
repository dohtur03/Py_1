import sys 

inp = sys.stdin.readline()
inp = inp.strip()
lngth = len(inp)
pointed = 0
stopper = 0
point = 0
order = 1
result = 0
left = 0
right = 0

if inp[0] == "-":
    first = 1
else:
    first = 0

for i in range(first, lngth):
    if (inp[i] < "0" or inp[i] > "9"):
        if (inp[i] == "." and pointed == 0):
            pointed += 1
            point = i
        else:
            stopper = 1
            print("NOOO")
                break

if stopper == 0:
    if pointed == 0:
        for i in range(lngth - 1, -1, -1):
            result += (int(inp[i]) * order * 2)
            order *= 10
            print(inp[i], result)
    else:
        for i in range(lngth - 1, point - 1, -1):
            

    

    print(f"string: {inp}, length: {lngth}, first char: {first}")


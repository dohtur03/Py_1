import sys
counter = []

def checker(inp):

    try:
        return int(inp)
    except ValueError:
        sys.stdout.write("nonono")
        return None
    
amount = sys.stdin.readline().strip()
am_checked = checker(amount)

if am_checked is not None:
    for i in range(0, am_checked):
        num = sys.stdin.readline().strip()
        if num not in counter:
            counter.append(num)

print(f"unique: {len(counter)}")

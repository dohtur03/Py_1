# Counts unique numbers in a string of numbers. Set usage.

def main():
    input_str = int(input().strip())
    result = unique(input_str)
    print(result)

def unique(input_str):
    counter = set()
    for _ in range(input_str):
        num = input().strip()
        counter.add(num)
    return len(counter)

if __name__ == "__main__":
    main()

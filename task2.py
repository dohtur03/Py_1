# Determine if a number is a palindrome 

def main():
    num = int(input())  
    result = process_num(num)
    print(result)

def process_num(num):
    digits = []
    palindrom = True
    temp = num

    while temp > 0:
        digit = (temp % 10)
        digits.append(digit)
        temp = temp // 10

    half = len(digits) // 2
    for i in range(half):
        if digits[i] != digits[-(i + 1)]:
            palindrom = False
            break
    return palindrom

if __name__ == "__main__":
    main()

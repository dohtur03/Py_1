import sys

digits = []
palindrom = True
num = int(sys.stdin.readline())
sys.stdout.write(f"{str(num)}\n")

while int(num) > 0:
    digit = (num % 10)
    print(digit)
    digits.append(digit)
    num = int(num / 10)

print(digits)
half = int(len(digits)/2)
for i in range(half):
    start = digits[i]
    end = digits[-(i + 1)]
    print(start, end)
    if start != end:
        palindrom = False
        print("OHOH, not PALINDROME!")
        break
print("OH, YES, PALINDROME!")



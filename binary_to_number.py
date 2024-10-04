import sys
binary = input("binary: ").strip()
base = 1
number = 0
for digit in binary[::-1]:
    try:
        digit = int(digit)
        if digit > 1 or digit < 0:
            raise ValueError
        if digit:
            number += base
    except ValueError:
        print(f"Invalid digit '{digit}' given, exiting.")
        sys.exit()
    base = base * 2
print(f"The binary digits: {binary} are equal to: {number}")
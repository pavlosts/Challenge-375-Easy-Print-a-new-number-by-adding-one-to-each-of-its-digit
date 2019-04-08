number = input()

digits = list(map(int, number))

digitsLength = len(digits)

for i in range(digitsLength):
    digits[i] += 1

result = "".join(list(map(str, digits)))

print(result)

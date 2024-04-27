total = 0
factorial = 1
i = 1
n = int(input('Enter a number: '))
while i <= n < 10 ** 6:
    factorial *= i
    total += 1 / factorial
    i += 1
e = 1 + total
print("The approximation of e is", e)

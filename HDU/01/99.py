y = 4224
sum = 0
while y > 0:
    digit = y % 10
    sum += digit
    y = y // 10
print(sum)
import math

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
s = (a + b + c) / 2
S = math.sqrt(s * (s - a) * (s - b) * (s - c))
print('三角形面积为', S)

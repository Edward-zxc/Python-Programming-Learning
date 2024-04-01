k = 2
n = 10
temp = k
length = 0
while k <= n:
    if k % temp == 0:
        length += 1
        print(k)
    k += 1
print(length)
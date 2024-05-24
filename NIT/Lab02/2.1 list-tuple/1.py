list_a = [1, 2, 3, 4, 5, 6]

# 方法一：使用切片进行反转
reversed_list1 = list_a[::-1]
print(reversed_list1)

# 方法二：使用reverse()方法

print(list_a)

# 方法三：Bubble sort
for i in range(len(list_a)):
    for j in  range(len(list_a) - i - 1):
        if list_a[j] > list_a[j+1]:
            list_a[j+1],list_a[j]=list_a[j],list_a[j+1]
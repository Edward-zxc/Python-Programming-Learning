def split_list(lst, n):
    avg = len(lst) / float(n)
    result = []
    last = 0.0
    while last < len(lst):
        result.append(lst[int(last):int(last + avg)])
        last += avg
    return result

# 示例
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 3
sublists = split_list(original_list, n)
print("原列表：", original_list)
print("子列表：", sublists)

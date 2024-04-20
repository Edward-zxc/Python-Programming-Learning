def remove_duplicates(lst):
    return list(set(lst))

# 示例
original_list = [1, 2, 3, 1, 4, 2, 5, 3]
print("原始列表：", original_list)
print("删除重复元素后的列表：", remove_duplicates(original_list))

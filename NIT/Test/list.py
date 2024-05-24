


# function2
def unique_list(lst):
    tmp = []
    for i in lst:
        if i not in tmp:
            tmp.append(i)
    return tmp


result = unique_list([1, 2, 2, 3, 1, "a", "a"])
print(result)

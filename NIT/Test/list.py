
# function2
def unique_list(list):
    tmp  = []
    for i in list:
        if i not in tmp:
            tmp.append(i)
    return tmp


result = unique_list([1,1,1,1,1])
print(result)

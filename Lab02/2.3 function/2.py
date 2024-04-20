def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

# 示例
print(multiply(2, 3, 4))  # 输出24

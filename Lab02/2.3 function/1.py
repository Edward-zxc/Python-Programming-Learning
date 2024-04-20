def convert_to_int(matrix):
    result = []
    for row in matrix:
        int_row = [int(element) for element in row]
        result.append(int_row)
    return result

# 示例
test_matrix = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
print(convert_to_int(test_matrix))

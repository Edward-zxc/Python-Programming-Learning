def shift_string(input_str):
    shifted_str = input_str[-1] + input_str[:-1]
    return shifted_str


input_str = "hello"
print(shift_string(input_str))

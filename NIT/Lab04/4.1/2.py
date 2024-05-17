
input_string = input("请输入一串字符串: ")


upper_case_string = input_string.upper()


with open('2.txt', 'w') as f:
    f.write(upper_case_string)

print("转换后的字符串已经写入到2.txt文件中。")

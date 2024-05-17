
with open('A.txt', 'r') as f:
    a_content = f.read()


with open('B.txt', 'r') as f:
    b_content = f.read()


c_content = a_content + b_content


with open('C.txt', 'w') as f:
    f.write(c_content)

print("文件合并已完成！请查看C.txt文件。")

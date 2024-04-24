def count_letters(string):
    letter_count = {}
    for char in string.lower():
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1
    return letter_count


input_string = "Hello, World!"
print("字符串中每个字母的出现次数：", count_letters(input_string))

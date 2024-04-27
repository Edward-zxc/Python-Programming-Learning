def find_middle_number(numbers):
    numbers.sort()
    return numbers[len(numbers) // 2]


numbers = [3, 1, 7, 4, 5]
print(find_middle_number(numbers))

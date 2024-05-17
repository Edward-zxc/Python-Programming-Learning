
with open('1.txt', 'r') as f:
    content = f.read()


numbers = [int(num) for num in content.split()]


sorted_numbers = sorted(numbers)
print(sorted_numbers)

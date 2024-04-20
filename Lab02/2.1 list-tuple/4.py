def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def remove_primes(lst):
    return [num for num in lst if not is_prime(num)]

# 示例
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(remove_primes(num_list))

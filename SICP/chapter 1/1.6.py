def sum_digits(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total


print(sum_digits(100))


def sum_cubes(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k * k * k, k + 1
    return total


print(sum_cubes(100))


def sum_pi(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + 8 / ((4 * k - 1) * (4 * k - 3)), k + 1
    return total


print(sum_pi(100))

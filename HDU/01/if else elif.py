def falling(n, k):
    result = 1
    for i in range(0, k):
        result *= (n - i)
    return result


# Example usage:
print(falling(6, 3))  # Output: 6 * 5 * 4 = 120


def falling(n, k):
    result = 1
    i = 0
    while i < k:
        result *= (n - i)
        i += 1
    return result


# Example usage:
print(falling(6, 3))  # Output: 6 * 5 * 4 = 120

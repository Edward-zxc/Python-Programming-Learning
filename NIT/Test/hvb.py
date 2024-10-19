def gcd(a, b):
    """计算最大公约数"""
    while b:
        a, b = b, a % b
    return a


def simplify_fraction(fraction):
    """化简分数"""
    num, den = fraction
    common_divisor = gcd(num, den)
    return (num // common_divisor, den // common_divisor)


def add_fractions(frac1, frac2):
    """分数加法"""
    num1, den1 = frac1
    num2, den2 = frac2
    return simplify_fraction((num1 * den2 + num2 * den1, den1 * den2))


def subtract_fractions(frac1, frac2):
    """分数减法"""
    num1, den1 = frac1
    num2, den2 = frac2
    return simplify_fraction((num1 * den2 - num2 * den1, den1 * den2))


def multiply_fractions(frac1, frac2):
    """分数乘法"""
    num1, den1 = frac1
    num2, den2 = frac2
    return simplify_fraction((num1 * num2, den1 * den2))


def divide_fractions(frac1, frac2):
    """分数除法"""
    num1, den1 = frac1
    num2, den2 = frac2
    return simplify_fraction((num1 * den2, den1 * num2))


def print_fraction(frac):
    """格式化输出分数"""
    num, den = frac
    return f"{num}/{den}"


def jacobi_iteration(A, b, x, iterations):
    """雅可比迭代法"""
    n = len(b)
    x_new = [(0, 1) for _ in range(n)]  # Initialize with 0

    for it in range(iterations):
        for i in range(n):
            sum_ax = (0, 1)  # Initialize as 0 (0/1)
            for j in range(n):
                if j != i:
                    sum_ax = add_fractions(sum_ax, multiply_fractions(A[i][j], x[j]))

            # Update x_new[i]
            x_new[i] = divide_fractions(subtract_fractions(b[i], sum_ax), A[i][i])

        x = x_new.copy()
        print(f"Iteration {it + 1}: {[print_fraction(xi) for xi in x]}")

    return x


def gauss_seidel_iteration(A, b, x, iterations):
    """高斯-赛德尔迭代法"""
    n = len(b)

    for it in range(iterations):
        for i in range(n):
            sum_ax = (0, 1)  # Initialize as 0 (0/1)
            for j in range(n):
                if j != i:
                    sum_ax = add_fractions(sum_ax, multiply_fractions(A[i][j], x[j]))

            # Update x[i]
            x[i] = divide_fractions(subtract_fractions(b[i], sum_ax), A[i][i])

        print(f"Iteration {it + 1}: {[print_fraction(xi) for xi in x]}")

    return x


# Coefficient matrix A and constant terms vector b
A = [
    [(20, 1), (2, 1), (3, 1)],
    [(1, 1), (8, 1), (1, 1)],
    [(2, 1), (-3, 1), (15, 1)]
]
b = [(25, 1), (10, 1), (14, 1)]

# Initial guess
initial_guess = [(0, 1), (0, 1), (0, 1)]

# Number of iterations
iterations = 5

# Run Jacobi iteration
print("Jacobi Iteration Results:")
jacobi_solution = jacobi_iteration(A, b, initial_guess, iterations)

# Run Gauss-Seidel iteration
print("\nGauss-Seidel Iteration Results:")
gauss_seidel_solution = gauss_seidel_iteration(A, b, initial_guess.copy(), iterations)

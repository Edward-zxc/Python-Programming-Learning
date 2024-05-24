def is_palindrome(s):
    return s == s[::-1]


n = str(input("Please input a string: "))
print(is_palindrome(n))

# function1 alternative
"""
def is_palindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
n = str(input("Please input a string: "))
print(is_palindrome(n))
"""

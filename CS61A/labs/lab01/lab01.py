"""
Q1:Control
py ok -q control -u --local
### python  because in Python, any non-zero value is considered True.
Q2:DEBUG
py ok -q debugging-quiz -u --local
"""


def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    '''
    py ok -q falling --local
    '''
    "*** YOUR CODE HERE ***"
    if k == 0:
        return 1
    else:
        return n * falling(n - 1, k - 1)


def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """
    '''
    py ok -q divisible_by_k --local
    '''
    "*** YOUR CODE HERE ***"
    if n >= k:
        count = 0
        tmp = k
        while tmp <= n:
            if tmp % k == 0:
                print(tmp)
                count += 1
            tmp += 1
        return count

    else:
        return 0


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    ''' 
    py ok -q double_eights --local
    '''
    "*** YOUR CODE HERE ***"
    def count8(temp):
        count1 = 0
        while temp >= 8:
            if temp % 10 == 8:
                count1 += 1
            temp //= 10
        return count1
    countForReal = count8(n)
    '''
    判断有几个数字8，以及有无数字8
    '''
    if n > 10 and countForReal >= 2:
        while n >= 8:
            if n % 10 == 8:
                n //= 10
                if n % 10 == 8:
                    return True
                else:
                    return False
            n //= 10
    else:
        return False

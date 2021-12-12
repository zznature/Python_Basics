def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    i = 1
    while a % b != 0:
        a = a * i
        i = i + 1
    return a * i



def unique_digits(n):
    """Return the number of unique digits in positive integer n

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"


def has_digit(n, k):

    # Hint: You may find it helpful to first define a function has_digit(n, k),
    # which determines whether a number n has digit k.
    while  n :
        pass
        if n % 10 = k
            return 1
        else n // 10**i
    
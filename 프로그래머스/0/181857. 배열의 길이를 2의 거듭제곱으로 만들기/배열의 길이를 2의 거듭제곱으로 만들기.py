def solution(arr):
    n = len(arr)

    # A power of two has exactly one 1 bit.
    # n & (n - 1) removes the rightmost 1 bit, so the result is 0
    # only when n is already a power of two.
    if n & (n - 1) == 0:
        return arr

    # For example, 6 is 110 and bit_length() is 3.
    # 1 << 3 is 1000 in binary, so the next power of two is 8.
    next_power = 1 << n.bit_length()

    return arr + [0] * (next_power - n)
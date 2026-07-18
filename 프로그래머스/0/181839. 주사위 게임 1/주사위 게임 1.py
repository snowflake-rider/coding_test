def solution(a, b):
    is_a_odd, is_b_odd = (a % 2 > 0), (b % 2 > 0)
    state = ((is_a_odd & 1) << 1) | (is_b_odd & 1)
    if state == 0b11:
        return a*a + b*b
    elif state >= 0b01:
        return 2*(a+b)
    else:
        return abs(a-b)
    
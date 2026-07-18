def solution(a, b):
    a_b, b_a = int(str(a)+str(b)), int(str(b)+str(a))
    return max(a_b, b_a)
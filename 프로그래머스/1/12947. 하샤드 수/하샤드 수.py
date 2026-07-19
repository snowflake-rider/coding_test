def solution(x):
    factor = sum(int(c) for c in str(x))
    return x % factor == 0
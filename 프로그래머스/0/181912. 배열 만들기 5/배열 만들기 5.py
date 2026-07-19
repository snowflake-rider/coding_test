def solution(intStrs, k, s, l):
    ints = [int(intStr[s:s+l]) for intStr in intStrs ]
    return [n for n in ints if n > k]
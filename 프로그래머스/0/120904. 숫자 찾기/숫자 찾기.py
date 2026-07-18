def solution(num, k):
    for i, c in enumerate(str(num)):
        if int(c) == k:
            return i + 1
    return -1
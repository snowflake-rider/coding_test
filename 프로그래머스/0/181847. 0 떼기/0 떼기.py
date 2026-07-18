def solution(n_str):
    # 1. find the first non-zero digit from left
    # 2. substring?
    first_non_zero = 0
    for i, c in enumerate(n_str):
        if int(c) > 0:
            first_non_zero = i
            break
    return n_str[first_non_zero:]
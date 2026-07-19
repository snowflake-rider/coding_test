def solution(str1, str2):
    # since len(str1)==len(str2)
    return "".join([c1+c2 for c1, c2 in zip(str1, str2)])
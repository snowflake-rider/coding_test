def solution(my_string, alp):
    return "".join([c.upper() if c == alp else c for c in list(my_string)])
def solution(my_string, indices):
    picks = sorted(set(range(len(my_string))) - set(indices))
    return "".join(my_string[i] for i in picks)
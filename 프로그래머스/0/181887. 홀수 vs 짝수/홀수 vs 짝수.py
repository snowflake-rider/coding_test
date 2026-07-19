def solution(num_list):
    evens, odds = sum(num_list[::2]), sum(num_list[1::2])
    return max(evens, odds)
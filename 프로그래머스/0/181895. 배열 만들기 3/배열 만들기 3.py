def solution(arr, intervals):
    first, second = intervals[0], intervals[1]
    return arr[first[0]:first[1]+1] + arr[second[0]:second[1]+1]
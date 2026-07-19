def solution(arr):
    # len(arr)==len(arr[0])
    n = len(arr)
    pairs = [(i,j) for i in range(n) for j in range(n)]
    for i, j in pairs:
        if i == j:
            continue
        if arr[i][j] != arr[j][i]:
            return 0
    return 1
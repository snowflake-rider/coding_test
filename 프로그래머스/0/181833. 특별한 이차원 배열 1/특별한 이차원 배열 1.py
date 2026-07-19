def solution(n):
    # 100 
    # 0{n} <- padding n 0s
    # b converts to binary num
    return [
        list(map(int, f"{1 << (n-1-i):0{n}b}"))
        for i in range(n)
    ]
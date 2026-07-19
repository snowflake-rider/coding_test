def solution(n):
    # n % x -> 1 
    # n = (x*y) + 1 => (n-1)=(x*y)
    # smallest x
    
    for x in range(2,int(n**0.5)+1):
        if (n-1) % x == 0:
            return x
    return (n-1)
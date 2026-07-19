from math import prod
def solution(a, b, c):
    
    dice = (a,b,c) 
    # CASE 1: all three nums different (lowest result case)
    # 5-len(set(dice)) = 5-3=2=>range(1,2) = 1 => (a+b+c)
    # CASE 2: two nums same 
    # (CASE 1) * (sum of squares)
    # 5-len(set(dice)) = 5-2=3=>range(1,3) = 1,2 => (a+b+c)+(a**2+b**2+c**2)
    # CASE 3: all diff
    # (CASE 2) * (sum of cubes)
    # 5-len(set(dice)) = 5-1=4=>range(1,4) = 1,2,3 => (a+b+c)+(a**2+b**2+c**2)+(a**3+b**3+c**3)
    
    return prod(
    sum(n ** p for n in dice)
        for p in range(1,5-len(set(dice)))
    )
    
    
    
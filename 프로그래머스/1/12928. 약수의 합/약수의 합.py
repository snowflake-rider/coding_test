def solution(n):
    factors_sum = 0
    for factor in range(1, int(n**0.5)+1):
        if n % factor == 0:
            factors_sum += (factor + (n // factor))
            factors_sum -= factor if (factor == n // factor) else 0
    return factors_sum
             
        
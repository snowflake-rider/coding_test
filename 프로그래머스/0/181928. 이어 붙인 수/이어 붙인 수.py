def solution(num_list):
    evens = int("".join([str(n) for n in num_list if n % 2 == 0]))
    odds = int("".join([str(n) for n in num_list if n % 2 > 0]))
    return evens+odds
    
        
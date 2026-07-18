import operator
def solution(binomial):
    x, op, y = binomial.split()
    ops = {
        "+":operator.add,"-":operator.sub,"*":operator.mul
    }
    return ops[op](int(x), int(y))
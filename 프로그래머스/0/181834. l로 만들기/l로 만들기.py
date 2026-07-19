
def solution(myString):
    def transform(c):
        return 'l' if c < 'l' else c
    return "".join((map(transform, list(myString))))
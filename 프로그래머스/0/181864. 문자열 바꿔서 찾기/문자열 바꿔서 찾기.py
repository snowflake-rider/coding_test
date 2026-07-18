def solution(myString, pat):
    return int(pat in "".join("A" if c == "B" else "B" for c in myString))
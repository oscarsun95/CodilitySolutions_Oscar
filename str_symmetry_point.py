def solution(S):
    # write your code in Python 3.6
    N = len(S)
    if N <= 1:
        return N - 1
    if N % 2 == 0:
        return -1
    begin = 0
    end = N - 1
    while begin < end:
        if S[begin] != S[end]:
            return -1
        begin += 1
        end -= 1
    return begin
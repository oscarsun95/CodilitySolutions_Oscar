def solution(K, A):
    # write your code in Python 3.6
    count = 0
    length = 0
    for a in A:
        length += a
        if length >= K:
            count += 1
            length = 0
    return count
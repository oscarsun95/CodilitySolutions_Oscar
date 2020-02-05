def solution(A, B):
    # write your code in Python 3.6
    N = len(A)
    if N <= 1:
        return N
    size = 1
    right = B[0]
    for i in range(1, N):
        if A[i] > right:
            right = B[i]
            size += 1
    return size
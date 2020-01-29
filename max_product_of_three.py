def solution(A):
    # write your code in Python 3.6
    A.sort()
    if len(A) == 3:
        return A[0] * A[1] * A[2]
    if A[-1] <= 0:
        return A[-1] * A[-2] * A[-3]
    if A[-2] <= 0 or A[-3] <= 0 or A[0] * A[1] >= A[-3] * A[-2]:
        return A[0] * A[1] * A[-1]
    return A[-1] * A[-2] * A[-3]
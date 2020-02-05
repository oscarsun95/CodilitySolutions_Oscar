def solution(A):
    # write your code in Python 3.6
    N = len(A)
    if N == 1:
        return 2 * abs(A[0])
    A.sort()
    if A[0] >= 0:
        return 2 * A[0]
    if A[-1] <= 0:
        return -2 * A[-1]
    back = 0
    front = N - 1
    result = A[-1] - A[0]
    while (back < front) and (A[back] <= 0 < A[front]):
        # print(back, front, result)
        f = A[front]
        b = -A[back]
        if b == f:
            return 0
        elif b > f:
            back += 1
            result = min(result, b-f)
        else:
            front -= 1
            result = min(result, f-b)
    for i, a in enumerate(A):
        if a > 0:
            result = min(result, 2 * a, -2 * A[i-1])
            break
    return result
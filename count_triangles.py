def solution(A):
    # write your code in Python 3.6
    N = len(A)
    if N <= 2:
        return 0
    A.sort()
    count = 0
    for i in range(N):
        k = i + 2
        for j in range(i+1, N):
            while (k < N) and (A[k] < A[i]+ A[j]):
                k += 1
            count += k - j - 1
    return count
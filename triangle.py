def solution(A):
    # write your code in Python 3.6
    A.sort()
    A = [a for a in A if a > 0]
    N = len(A)
    if N <= 2:
        return 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1, N):
                if A[i] + A[j] > A[k]:
                    return 1
                else:
                    break
    return 0
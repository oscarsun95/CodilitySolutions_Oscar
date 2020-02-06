def fibonacci(N):
    fib = [0] * N
    fib[0] = 1
    fib[1] = 1
    for i in range(2, N):
        fib[i] = fib[i-1] + fib[i-2]
    return fib
    
def solution(A, B):
    # write your code in Python 3.6
    M = max(A)
    fib = fibonacci(M+1)
    N = len(A)
    res = [0] * N
    for i in range(N):
        res[i] = fib[A[i]] & ((1 << B[i]) - 1)
    return res
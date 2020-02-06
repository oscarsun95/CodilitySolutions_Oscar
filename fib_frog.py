def fibonacci(n):
    fib = [1]
    a = fib[0]
    b = 1
    while a+b <= n:
        fib.append(a+b)
        a, b = b, a + b
    return fib

def solution(A):
    # write your code in Python 3.6
    if len(A) == 0:
        return 1
    A = [1] + A + [1]
    N = len(A)
    fib = fibonacci(N)
    if fib[-1] == N - 1:
        return 1
    # print(fib)
    reach = [-1] * N
    reach[0] = 0
    for i in range(1, N):
        if A[i] == 1:
            for f in fib:
                # print(i, f, reach)
                back_step = i - f
                if back_step >= 0:
                    if reach[back_step] >= 0:
                        if reach[i] == -1:
                            reach[i] = reach[back_step] + 1
                        else:
                            reach[i] = min(reach[back_step] + 1, reach[i])
                else:
                    break

    return reach[-1]
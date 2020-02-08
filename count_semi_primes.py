def get_sieve(n):
    sieve = [True] * (n + 1)
    if n == 0:
        return [False]
    sieve[0] = sieve[1] = False
    i = 2
    while i * i <= n:
        if sieve[i]:
            k = i * i
            while k <= n:
                sieve[k] = False
                k += i
        i += 1
    return sieve

def solution(N, P, Q):
    # write your code in Python 3.6
    sieve = get_sieve(N // 2)
    # print(sieve)
    # print([i for i, a in enumerate(sieve) if a])
    semi = [0] * (N + 1)
    for i in range(2, N + 1):
        if i * i > N:
            break
        for j in range(i, N // i + 1):
            # print(i, j)
            if sieve[i] and sieve[j]:
                semi[i * j] = 1
    # print(semi)
    for i in range(3, N + 1):
        semi[i] += semi[i-1]
    # print(semi)
    res = [0] * len(P)
    for i in range(len(P)):
        res[i] = semi[Q[i]] - semi[P[i]-1]
    return res
def solution(N):
    # write your code in Python 3.6
    min_peri = 2 * (N + 1)
    i = 2
    while i * i <= N:
        if N % i == 0:
            peri = 2 * (i + N // i)
            min_peri = min(min_peri, peri)
        i += 1
    return min_peri
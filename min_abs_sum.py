def solution(A):
    # write your code in Python 3.6
    if len(A) == 0:
        return 0
    A = [abs(a) for a in A]
    # A.sort()
    M = max(A)
    count = [0] * (M + 1)
    for a in A:
        count[a] += 1
    S = sum(A)
    dp = [-1] * (S + 1)
    dp[0] = 0
    for a, n in enumerate(count):
        if n > 0:
            for s in range(S):
                if dp[s] >= 0:
                    dp[s] = n
                elif s >= a and dp[s-a] > 0:
                    dp[s] = dp[s-a] - 1
    # print(dp)
    for half in range(S // 2, -1, -1):
        if dp[half] >= 0:
            return S - 2 * half
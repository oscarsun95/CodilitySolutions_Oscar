def get_factors(N):
    factors = []
    i = 1
    while i * i < N:
        if N % i == 0:
            factors.extend([i, N // i])
        i += 1
    if i * i == N:
        factors.append(i)
    return sorted(factors, reverse=True)
    
def solution(A):
    # write your code in Python 3.6
    N = len(A)
    if N <= 2:
        return 0
    peaks = [0] * N
    total = 0
    for i in range(1, N - 1):
        if (A[i] > A[i-1]) and (A[i] > A[i+1]):
            total += 1
        peaks[i] = total
    peaks[-1] = total
    # print(peaks)
    if total <= 1:
        return total
    else:
        factors = get_factors(N)
        # print(factors)
        if len(factors) <= 2:
            return 1
        else:
            for n in factors:
                length = N // n
                if length <= 2:
                    continue
                for j in range(length-1, N, length):
                    # print(j, length)
                    start = max(j-length, 0)
                    if peaks[start] == peaks[j]:
                        break
                    if j == N-1:
                        return n
        return n
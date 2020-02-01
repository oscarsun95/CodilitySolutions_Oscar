def solution(A):
    # write your code in Python 3.6
    N = len(A)
    if N <= 2:
        return 0
    peak_dists = []
    last_peak = None
    for i in range(1, N-1):
        if (A[i] > A[i-1]) and (A[i] > A[i+1]):
            if last_peak is None:
                peak_dists.append(0)
            else:
                peak_dists.append(peak_dists[-1] + i - last_peak)
            last_peak = i
    # print(peak_dists)
    K = len(peak_dists)
    if K <= 1:
        return K
    else:
        k = 1
        result = 0
        while k * (k - 1) <= peak_dists[-1]:
            num = 1
            i = 1
            start = peak_dists[0]
            while (num < k) and (i < K):
                # print(k, i, start, num, result)
                if peak_dists[i] - start >= k:
                    num += 1
                    start = peak_dists[i]
                i += 1
            result = max(result, num)
            k += 1
        return result
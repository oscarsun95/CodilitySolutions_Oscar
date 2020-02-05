def check(A, max_size):
    cnt = 1
    size = A[0]
    for a in A[1:]:
        if size + a > max_size:
            cnt += 1
            size = a
        else:
            size += a
    return cnt

def solution(K, M, A):
    # write your code in Python 3.6
    N = len(A)
    M = max(A)
    if K >= N or M == 0:
        return M
    begin = M
    end = sum(A)
    result = end
    while begin <= end:
        mid = (begin + end) // 2
        if check(A, mid) <= K:
            end = mid - 1
            result = mid
        else:
            begin = mid + 1
    return result
def get_prefix_nail_sum(nails, M):
    nail_sum = [0] * (M+1)
    for nail in nails:
        nail_sum[nail] += 1
    for i in range(1, M+1):
        nail_sum[i] += nail_sum[i-1]
    return nail_sum

def check(A, B, pref):
    N = len(A)
    for i in range(N):
        if pref[B[i]] == pref[A[i]-1]:
            return False
    return True
    
def solution(A, B, C):
    # write your code in Python 3.6
    M = len(C)
    begin = 0
    end = M
    result = -1
    while begin <= end:
        mid = (begin + end) // 2
        if mid == 0:
            pref_sum = get_prefix_nail_sum([C[0]], 2*M)
        else:
            pref_sum = get_prefix_nail_sum(C[:mid], 2*M)
        # print(begin, end, mid ,pref_sum)
        if check(A, B, pref_sum):
            end = mid -1
            result = max(1, mid)
        else:
            begin = mid + 1
    return result
def solution(A):
    # write your code in Python 3.6
    N = len(A)
    if N == 3:
        return 0
    max_ending = 0 
    max_left = 0
    max_slice = A[1]
    for i in range(2, N-1):
        max_left = max(A[i-1], max_left + A[i-1])
        max_ending = max(max_left, max_ending + A[i], A[i])
        max_slice = max(max_slice, max_ending)
    return max(max_slice, 0)
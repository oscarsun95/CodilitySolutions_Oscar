def solution(A):
    # write your code in Python 3.6
    if len(A) == 1:
        return A[0]
    max_ending = 0 
    max_slice = A[0]
    for a in A:
        max_ending = max(a, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice

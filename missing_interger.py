def solution(A):
    # write your code in Python 3.6
    M = max(A)
    if M <= 0:
        return 1
    A.sort()
    A = [a for a in A if a >0]
    last = A[0]
    if last != 1:
        return 1
    if len(A) == 1:
        return 2
    for a in A[1:]:
        if a == last:
            continue
        if a - last != 1:
            return last + 1
        last = a
    return A[-1] + 1
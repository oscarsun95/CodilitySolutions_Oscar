def solution(A):
    # write your code in Python 3.6
    N = len(A)
    if N <= 2:
        return 0
    stack = [A[0]]
    curmax = 0
    for i in range(1, N):
        if A[i] > stack[0]:
            if len(stack) > 1:
                curmax = max(curmax, min(stack[0], A[i]) - stack[-1])
            stack = [A[i]]
        else:
            if stack[-1] < A[i]:
                curmax = max(curmax, min(A[i], stack[0]) - stack[-1])
            elif stack[-1] > A[i]:
                stack.append(A[i])
    return curmax     
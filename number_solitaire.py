def solution(A):
    # write your code in Python 3.6
    maximals = [A[0]]
    for a in A[1:-1]:
        # maximal sum at step len(maximals)-1
        maximals.append(max(maximals) + a)
        if len(maximals) > 6:
            maximals.pop(0)
    return max(maximals) + A[-1]
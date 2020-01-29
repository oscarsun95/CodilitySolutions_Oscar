def solution(A, B):
    # write your code in Python 3.6
    N = len(A)
    if N == 1:
        return N
    count = N
    down_fish = []
    for i in range(N):
        if B[i] == 1:
            down_fish.append(A[i])
        else:
            n = len(down_fish)
            if n >= 1:
                for _ in range(n):
                    df = down_fish[-1]
                    if df > A[i]:
                        count -= 1
                        break
                    else:
                        count -= 1
                        down_fish.pop(-1)
    return count
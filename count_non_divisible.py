def solution(A):
    # write your code in Python 3.6
    N = len(A)
    B = [0] * (2 * N + 1)
    for a in A:
        B[a] += 1
    total = 0
    C = [0] * (2 * N + 1)
    for i in range(1, 2 * N + 1):
        if B[i] == 0:
            continue
        else:
            total += B[i]
        # C[i] += N - total
        # for j in range(i):
        #     if j !=0 and i % j != 0:
        #         C[i] += B[j]
        j = 2
        count = B[1]
        if i > 1:
            count += B[i]
        while j * j < i:
            if i % j == 0:
                count += B[j] + B[i // j]
            j += 1
        if j * j == i:
            count += B[j]
        # print(i, count, B[i])
        C[i] += N -count
    res = [0] * N
    for i in range(N):
        res[i] = C[A[i]]
    return res
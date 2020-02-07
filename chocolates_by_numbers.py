def solution(N, M):
    # write your code in Python 3.6
    if M == 1 or N == 1:
        return N
    count = 0
    start = 0
    while 1:
        count += (N -start) // M
        start = (N - start) % M
        # print(count, start)
        if start == 0:
            break
        else:
            start = M - start
        count += 1
    return count
def solution(N, A):
    # write your code in Python 3.6
    count = {}
    max_count = 0
    for a in A:
        if a == N+1:
            if len(count) >= 1:
                max_count += max(count.values())
            count = {}
        else:
            if count.get(a):
                count[a] += 1
            else:
                count[a] = 1
    # print(count, max_count, max_map)
    counter = [0] * N
    for i in range(N):
        counter[i] = max_count + count.get(i+1, 0)
    return counter
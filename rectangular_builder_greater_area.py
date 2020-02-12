def solution(A, X):
    # write your code in Python 3.6
    N = len(A)
    if N < 4:
        return 0
    C = {}
    for a in A:
        C[a] = C.get(a, 0) + 1
    count = 0
    # print(C)
    fences = []
    for i in C:
        if C[i] < 2:
            continue
        else:
            fences.append(i)
            if C[i] >= 4:
                if i * i >= X:
                    count += 1
    fences.sort()
    L = len(fences)
    # print(fences, count)
    for i in range(L):
        begin = i + 1
        end = L - 1
        # print(begin, end)
        while begin <= end:
            mid = (begin + end) // 2
            if fences[mid] * fences[i] >= X:
                end = mid - 1
            else:
                begin = mid + 1
                
        count += L - 1 - end
        if count > 1000000000:
            return -1
    # print(count)
    return count
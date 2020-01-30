def get_index_leader(A):
    index = {}
    index_leader = [None] * len(A)
    candidate = None
    max_count = 0
    for i, a in enumerate(A):
        if a in index:
            index[a] += 1
        else:
            index[a] = 1
        if index[a] > max_count:
            max_count = index[a]
            candidate = a
        # print(index, max_count, candidate)
        if max_count > (i + 1) // 2 and (candidate is not None):
            index_leader[i] = candidate
    return index_leader

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    if N == 1:
        return 0
    front_leader = get_index_leader(A)
    end_leader = get_index_leader(A[::-1])
    # print(front_leader)
    # print(end_leader)
    count = 0
    for i in range(N-1):
        # print(front_leader[i], end_leader[N-i-2], count)
        if (front_leader[i] == end_leader[N-i-2]) and (front_leader[i] is not None) and (end_leader[N-i-2] is not None):
            
            count += 1
    return count
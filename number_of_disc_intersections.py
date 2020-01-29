def solution(A):
    # write your code in Python 3.6
    starts = {}
    ends = {}
    for i, a in enumerate(A):
        s = i - a
        e = i + a
        if s in starts:
            starts[s] += 1
        else:
            starts[s] = 1
        if e in ends:
            ends[e] += 1
        else:
            ends[e] = 1
    points = sorted(set(starts).union(set(ends)))
    count = 0
    actives = 0
    for p in points:
        ns = starts.get(p, 0)
        count += (2 * actives + ns-1) * ns // 2
        actives +=  ns- ends.get(p, 0)
    if count > 10000000:
        count = -1
    return count 
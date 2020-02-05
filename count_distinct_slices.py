def solution(M, A):
    # write your code in Python 3.6
    # As every time we extend the range, all the possible length of the slices before extension will have one more move and one new slice, the length of which is the same as the extended range, can be added.

    total = 0
    back = -1
    has = [-1] * (M + 1)
    for front, a in enumerate(A):
        if has[a] > back:
            back = has[a]
        total += front - back
        has[a] = front
        # print(back, front, total, has)
    return min(total, 1000000000)
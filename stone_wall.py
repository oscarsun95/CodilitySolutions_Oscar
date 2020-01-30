def solution(H):
    # write your code in Python 3.6
    N = len(H)
    if N == 1:
        return 1
    count = N
    heights = [H[0]]
    for i in range(1, N):
        # print(H[i], heights, count)
        while (len(heights) > 0) and (heights[-1]) > H[i]:
            heights.pop()
        if (len(heights) > 0) and (heights[-1] == H[i]):
            count -= 1
        else:
            heights.append(H[i])
    return count
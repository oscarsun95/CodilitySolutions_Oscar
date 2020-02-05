def solution(A):
    # write your code in Python 3.6
    N = len(A)
    back = 0
    front = 0
    count = 1
    set_A = [A[0]]
    while front + 1 < N:
        if A[front+1] > A[front]:
            count += 1
            set_A.append(A[front+1])
        front += 1
    # print(front, count)
    A = set_A
    front = len(set_A) - 1
    while A[back] <= 0 < A[front] and back < front:
        f = A[front]
        b = A[back]
        # print(b, f)
        if b < 0:
            b = -b
        if b == f: 
            count -= 1
            back += 1
            front -= 1
        elif b > f:
            back += 1
        else:
            front -= 1
    return count
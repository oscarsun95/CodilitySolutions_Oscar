def solution(A):
    # write your code in Python 3.6
    min_start_index = 0
    min_average = (A[0] + A[1]) / 2
    for i in range(len(A)-2):
        average = (A[i] + A[i+1]) / 2
        if A[i+2] < average:
            average = (A[i] + A[i+1] + A[i+2]) / 3
        if average < min_average:
            min_average = average 
            min_start_index = i
    average = (A[-1] + A[-2]) / 2
    if average < min_average:
        min_start_index = len(A)-2
    return min_start_index